import contextlib
import inspect
import io
import logging
import os
import sys
import time
import unittest
from typing import Callable, Dict, Iterable, Union, Any

from tabulate import tabulate
from timeout_decorator import timeout

from mygrader import src
from mygrader.template import template


class Tester(unittest.TestCase):
    """
    A test class to run tests on user-defined functions.

    Attributes:
        year (str): The year for which the tests are being run (e.g., "y2023").
        runtime_limit (float): The maximum runtime allowed for a function.
        log_option (str): The logging option ("print" or "write") for the test summary.
        debug (bool): If True, enable debug mode for additional information.
    """

    def __init__(
            self,
            year: int,
            runtime_limit: Union[float, int] = 1.0,
            log_option: str = 'print',
            debug: bool = False
    ) -> None:
        """
        Initialize the Tester class.

        Args:
            year (int): The year for which the tests are being run (e.g., 2023).
            runtime_limit (float): The maximum runtime allowed for a function.
            log_option (str): The logging option ("print" or "write") for the test summary.
            debug (bool): If True, enable debug mode for additional information.
        """
        super().__init__()
        self.year: str = f'y{year}'
        self.runtime_limit: Union[float, int] = runtime_limit
        self.log_option: str = log_option
        self.debug: bool = debug

    @timeout(10)  # Timeout after 10 seconds to avoid too many test cases being generated
    def run_test(self, user_func: Callable, num_test_cases: int = 100, show_table: bool = False) -> None:
        """
        Run tests for the specified function using generated test cases.

        Args:
            user_func (Callable): The user-defined function to be tested.
            num_test_cases (int): The number of test cases to generate and run.
            show_table (bool): Whether to show the table of failed cases.

        Raises:
            ValueError: If an invalid option is provided.
            AttributeError: If an invalid function name is provided.

        Note:
            This method generates test cases, compares function outputs, and calculates success rate.
            Test results can be printed or written to a file based on provided options.

        Example:
            >>> from mygrader import mygrader
            >>> tester = Tester(runtime_limit=4, log_option="print")
            >>> func = lambda x: x + 1
            >>> tester.run_test(func)

        """
        func_name = user_func.__name__

        try:
            test_module = getattr(src, self.year)
            solver = getattr(test_module.Solution, func_name)
            return_type = self.return_type(user_func)
            solver_return = self.return_type(solver)

            if return_type != solver_return:
                raise ValueError(f"Mismatched return type expected: {solver_return}, got: {return_type}")

            if not 1 <= num_test_cases <= 1_000_000:
                logging.warning(f"Invalid number of test cases: {num_test_cases}")
                raise ValueError("The number of test cases should be between 1 and 1,000,000.")

            @timeout(self.runtime_limit)
            def get_random_test_case():
                return getattr(test_module.Generator, f"{func_name}_test_cases")(num_test_cases)

            test_cases_params = get_random_test_case()

            if self.debug:
                self.__print_debug_info(func_name, return_type, num_test_cases)

            result = self.__run_test_case(user_func, solver, test_cases_params, num_test_cases, return_type)

            formatted_summary_data = self.__generate_summary(result, show_table)
            self.__handle_log_option(formatted_summary_data)

        except AttributeError as e:
            raise AttributeError(f"Invalid function name: {user_func.__name__}") from e

        except ValueError as e:
            raise ValueError(f"Invalid option: {e}") from e

    @classmethod
    def return_type(cls, func: Callable) -> str:
        """
        Get the return type of the given function.

        This method takes a callable function as input and returns a string representation
        of its return type based on its signature's return annotation.

        Args:
            func (Callable): The function to be analyzed.

        Returns:
            str: The return type of the given function.

        Example:
            >>> def add(a: int, b: int) -> int:
            ...     return a + b
            ...
            >>> Tester.return_type(add)
            'int'
        """
        original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')  # Redirect stdout to null device
        _type = None

        try:
            signature = inspect.signature(func)
            return_annotation = signature.return_annotation

            if return_annotation is inspect.Signature.empty:
                generator = getattr(src.Generator, f"{func.__name__}_test_cases")
                sample = generator(1)
                return_annotation = type(func(*sample[0]))

            _type = 'None' if str(return_annotation) == "<class 'NoneType'>" else str(return_annotation)

        except AttributeError:
            raise AttributeError(f"Function not found in the Generator class: {func.__name__}")

        finally:
            sys.stdout = original_stdout  # Restore original stdout

        return _type

    @classmethod
    def capture_printed_text(cls, func: Callable, *args: Iterable) -> str:
        """
        Capture the printed output of a function.

        Args:
            func (Callable): The function to capture the printed output from.
            *args: Arguments to pass to the function.

        Returns:
            str: The captured printed text.

        Note:
            This method uses a StringIO buffer and the contextlib.redirect_stdout
            context manager to capture the printed output of the provided function.

        Example:
            >>> captured_text = Tester.capture_printed_text(print, "Hello, world!")
            >>> print(captured_text)
            Hello, world!

        """
        # Create a StringIO object to capture the printed text
        buffer = io.StringIO()

        # Use the redirect_stdout context manager to capture printed output
        with contextlib.redirect_stdout(buffer):
            # Call the function with the provided arguments and keyword arguments
            func(*args)

        # Get the captured printed text
        printed_text: str = buffer.getvalue()

        return printed_text

    @staticmethod
    def __generate_summary(
            summary_data: Dict, show_table: bool = False
    ) -> str:
        """
        Generate a summary based on the provided summary data and template.

        Args:
            summary_data (Dict): Dictionary containing summary data.
            show_table (bool): Whether to show the table of failed cases.

        Returns:
            str: The formatted summary.

        Raises:
            FileNotFoundError: If the template format is not found.
            Exception: If an error occurs while generating the summary.

        Note:
            This method generates a summary using the provided summary data and a template.
            It fills in placeholders in the template with the relevant information from the summary data.
            The generated summary can include a table of failed cases if show_table is True.
        """
        try:
            headers = ["Input", "Expected Output", "Actual Output"]
            table = []
            if show_table:
                for case in summary_data["failed_cases"]:
                    table.append([case["input"], f'{case["expected"]}'[:10], case["result"]][:10])
            else:
                table = [["", "", ""]]

            summary = template.format(
                failed_cases_table=tabulate(table, headers=headers, tablefmt="grid") if show_table else "",
                **{f"{key}": summary_data[key] for key in summary_data.keys() if key != "failed_cases"},
                more_info="Table is disabled" if not show_table else "",
            )

        except FileNotFoundError as e:
            print(f"Error: {e}")
            print(f"Error at line {e.__traceback__.tb_lineno}")
            raise FileNotFoundError("Template file not found. Please make sure that the template file exists.") from e

        except Exception as e:
            print(f"Error: {e}")
            print(f"Error at line {e.__traceback__.tb_lineno}")
            raise Exception("An error occurred while generating the summary.") from e

        return summary

    @staticmethod
    def __print_debug_info(func_name, return_type, num_test_cases):
        """
        Print debug information.

        Args:
            func_name (str): The name of the function being tested.
            return_type (str): The return type of the function being tested.
            num_test_cases (int): The number of test cases being generated.
        """
        logging.debug(f"Function name: {func_name}")
        logging.debug(f"Return type: {return_type}")
        logging.debug(f"Number of test cases: {num_test_cases}")

    def __handle_log_option(self, formatted_summary_data):
        """
        Handle the logging option for the test summary.

        Args:
            formatted_summary_data (str): The formatted summary data.

        Raises:
            ValueError: If an invalid logging option is provided.
        """
        if self.log_option == "print":
            print(formatted_summary_data)

        elif self.log_option == "write":
            with open(f"{self.year}_test_summary.txt", "w") as f:
                f.write(formatted_summary_data)

        else:
            raise ValueError(f"Invalid logging option: {self.log_option}")

    def __run_test_case(self, user_func, solver, test_cases_params, num_test_cases, return_type):
        """
        Run test cases and compare function outputs.

        Args:
            user_func (Callable): The user-defined function to be tested.
            solver (Callable): The solution function to be tested against.
            test_cases_params (Iterable): The parameters for the test cases.
            num_test_cases (int): The number of test cases to generate and run.

        Returns:
            Dict: A dictionary containing the test results.

        Raises:
            ValueError: If the function output does not match the expected output.
            TimeoutError: If the function exceeds the runtime limit.
        """

        @timeout(self.runtime_limit / (num_test_cases * 2))
        def runner(func: Callable, *_params: Iterable) -> Any:
            if return_type == "None":
                return self.capture_printed_text(func, *_params)
            return func(*_params)

        start_time = time.time()

        result = {
            "num_test_cases": num_test_cases,
            "passed_count": 0,
            "failed_count": 0,
            "failed_cases": []
        }

        for params in test_cases_params:
            try:
                user_output = runner(user_func, *params)
                solver_output = runner(solver, *params)

                if user_output == solver_output:
                    result["passed_count"] += 1
                else:
                    result["failed_count"] += 1
                    result["failed_cases"].append({
                        "input": params,
                        "expected": solver_output,
                        "result": user_output
                    })

            except TimeoutError:
                result["failed_count"] += 1
                result["failed_cases"].append({
                    "input": params,
                    "expected": "Timeout",
                    "result": "Timeout"
                })

            except Exception as e:
                result["failed_count"] += 1
                result["failed_cases"].append({
                    "input": params,
                    "expected": "Error",
                    "result": f"Error: {e}"
                })

        end_time = time.time()

        result["success_rate"] = (result["passed_count"] / result["num_test_cases"]) * 100
        result["total_time_result"] = end_time - start_time
        result["average_time"] = result["total_time_result"] / result["num_test_cases"]
        result["test_per_second"] = result["num_test_cases"] / result["total_time_result"]

        return result

    def __dir__(self) -> Iterable[str]:
        """
        Return the list of available functions for the given year.

        Returns:
            Iterable[str]: List of available functions.

        Note:
            This method inspects the module corresponding to the given year and retrieves a list of function names.
            Function names starting with "__" are excluded from the list.

        Example:
            >>> tester = Tester(2023)

            >>> available_functions = tester.__dir__()
            >>> print(available_functions)
        """
        return [func for func in dir(getattr(src, self.year)) if not func.startswith("__")]

    def __repr__(self) -> str:
        """
        Return a string representation of available functions for the given year.

        Returns:
            str: A formatted string listing available functions.

        Note:
            This method generates a string containing information about the available functions for the specified year.
            It retrieves the list of available functions using the __dir__ method.

        Example:
            >>> tester = Tester(2023)
            >>> representation = repr(tester)
            >>> print(representation)
            Available functions for 2023: ['function1', 'function2', ...]
        """
        return f"Available functions for {self.year}: {self.__dir__()}"

    def __str__(self) -> str:
        """
        Return a string representation of the Tester class for the given year.

        Returns:
            str: A formatted string describing the Tester class.

        Note:
            This method generates a string containing information about the Tester class, including the year for which
            the tests are being conducted. Additional information can be added as needed.

        Example:
            >>> tester = Tester(2023)
            >>> description = str(tester)
            >>> print(description)
            Tester class for the year 2023
        """
        return f"Tester class for the year {self.year}"
