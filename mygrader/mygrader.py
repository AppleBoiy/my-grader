import contextlib
import inspect
import io
import sys
import time
import unittest
from typing import Callable, Dict, Iterable, Union

from tabulate import tabulate
from timeout_decorator import timeout
from tqdm import tqdm

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

    def run_test(
            self,
            user_func: Callable,
            num_test_cases: int = 100,
            show_table: bool = False,
    ) -> None:
        """
        Run tests for the specified function using generated test cases.

        Args:
            user_func (Callable): The user-defined function to be tested.
            num_test_cases (int): The number of test cases to generate and run.
            show_table (bool): Whether to show the table of failed cases.

        Raises:
            ValueError: If an invalid option is provided.

        Note:
            This method generates test cases using the appropriate generator function
            for the given user-defined function. It compares the output of the user
            function with the expected output from the src class and calculates
            the success rate. The test results can be printed or written to a file
            based on the provided options.

        Example:
            >>> from mygrader import mygrader

            >>> # Create a Tester object (runtime_limit is optional)
            >>> opt = "print" # Output options ("print" or "write")
            >>> tester = Tester(runtime_limit=4, log_option=opt)
            >>> func = lambda x: x + 1 # User-defined function to be tested

            >>> tester.run_test(func)

        """

        func_name = user_func.__name__

        try:
            # TODO: Add support for multiple functions
            test_module = getattr(src, self.year)

            solver = getattr(test_module.Solution, func_name)
            return_type = self.return_type(solver)

            if num_test_cases < 1:
                raise ValueError("Number of test cases must be greater than 0.")
            elif num_test_cases > 1_000_000:
                raise ValueError("Too many test cases. Please reduce the number of test cases.")
            else:
                @timeout(5)
                def get_random_test_case():
                    return getattr(test_module.Generator, f"{func_name}_test_cases")(num_test_cases)

                try:
                    test_cases_params = get_random_test_case()
                except TimeoutError:
                    raise TimeoutError(f"Runtime limit exceeded for when generating test cases for {func_name}().")

            if self.debug:
                print(f'Function: {func_name}')
                print(f'Runtime limit: {self.runtime_limit} seconds')
                print(f'Year: {self.year}')
                print(f'Logging option: {self.log_option}')
                print(f'Expected return type: {return_type}')

                print(f'Testing... {func_name}() with {num_test_cases} test cases.')

            @timeout(self.runtime_limit)
            def run_test_case():
                start_time = time.time()
                _passed_count = 0
                _failed_count = 0
                _failed_cases = []

                for case in tqdm(range(num_test_cases), desc="Running tests", unit="test"):
                    _input = test_cases_params[case]

                    if return_type == "None":
                        _expected = self.capture_printed_text(solver, *_input)
                        _result = self.capture_printed_text(user_func, *_input)
                    else:
                        _expected = solver(*_input)
                        _result = user_func(*_input)

                    if _expected == _result:
                        _passed_count += 1
                    else:
                        _failed_count += 1
                        _failed_cases.append({
                            "input": _input,
                            "expected": _expected,
                            "result": _result
                        })

                _total_time = time.time() - start_time

                return {
                    "passed_count": _passed_count,
                    "failed_count": _failed_count,
                    "total_time_result": _total_time,
                    "average_time": _total_time / num_test_cases,
                    "failed_cases": _failed_cases[:10],
                    "test_per_second": num_test_cases / _total_time,
                    "success_rate": (_passed_count / num_test_cases) * 100,

                }

            # TODO: More options for logging, e.g., JSON, CSV, etc.
            try:
                result = run_test_case()

            except TimeoutError:
                raise TimeoutError(f"Runtime limit exceeded for when run test cases for {func_name}().")

            formatted_summary_data = self.__generate_summary(result, show_table)

            if self.log_option == "print":
                print(formatted_summary_data)
            elif self.log_option == "write":
                with open("test_summary.md", "w") as f:
                    f.write(formatted_summary_data)
            elif self.log_option == "None":
                return
            else:
                raise ValueError(f"Invalid option: {self.log_option}")

        except AttributeError:
            info = sys.exc_info()
            raise AttributeError(f"Invalid function name: {user_func.__name__}") from info[1]

    @classmethod
    def return_type(cls, func: Callable) -> str:
        """
        Return the return type of the given function.

        This method takes a callable function as input and returns a string representation
        of its return type based on its signature's return annotation.

        Args:
            func (Callable): The function to be tested.

        Returns:
            str: The return type of the given function.

        Example:
            >>> def add(a: int, b: int) -> int:
            ...     return a + b
            ...
            >>> Tester.return_type(add)
            'int'
        """
        signature = inspect.signature(func)
        return_annotation = signature.return_annotation

        return str(return_annotation)

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
