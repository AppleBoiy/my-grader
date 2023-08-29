import contextlib
import inspect
import io
import logging
import os
import sys
import time
import unittest
from multiprocessing import Process, Queue
from typing import Callable, Dict, Iterable, Any

from tabulate import tabulate
from tqdm import tqdm

from mygrader import src, template


class Tester(unittest.TestCase):
    """
    A tests class to run tests on user-defined functions.

    Attributes:
        year (str): The year for which the tests are being run (e.g., "y2023").
        log_option (str): The logging option ("print" or "write") for the tests summary.
        debug (bool): If True, enable debug mode for additional information.
    """

    def __init__(
            self,
            year: int,
            log_option: str = 'print',
            debug: bool = False,
            runtime_limit: int = 1
    ) -> None:
        """
        Initialize the Tester class.

        Args:
            year (int): The year for which the tests are being run (e.g., 2023).
            log_option (str): The logging option ("print" or "write") for the tests summary.
            debug (bool): If True, enable debug mode for additional information.
            runtime_limit (int): The maximum runtime limit (in seconds) for each tests case execution.

        Note:
            The `runtime_limit` parameter defines the maximum time a tests case execution is allowed to take.
            If a test case execution exceeds this limit, it will be terminated and considered as a TimeoutError.
        """
        super().__init__()
        self.year: str = f'y{year}'
        self.log_option: str = log_option
        self.debug: bool = debug
        self.runtime_limit: int = runtime_limit

    def run_test(
            self,
            user_func: Callable,
            num_test_cases: int = 100,
            more_detail: bool = False,
            show_table: bool = False,
    ) -> None:
        """
        Run tests for the specified function using generated tests cases.

        Args:
            user_func (Callable): The user-defined function to be tested.
            num_test_cases (int): The number of tests cases to generate and run.
            show_table (bool): Whether to show the table of failed cases.
            more_detail (bool):

        Raises:
            ValueError: If an invalid option is provided.
            AttributeError: If an invalid function name is provided.
            TimeoutError: If the function execution exceeds the timeout.

        Note:
            This method generates test cases, compares function outputs, and calculates success rate.
            Test results can be printed or written to a file based on provided options.

            If a test case execution takes more than the specified runtime_limit (in seconds),
            the function will raise a TimeoutError and terminate.

        Example:
            >>> from mygrader import mygrader
            >>> tester = Tester(year=2023, runtime_limit=5)
            >>> def add(a, b):
            ...     return a + b
            ...
            >>> tester.run_test(add, num_test_cases=50)
        """

        func_name = user_func.__name__

        try:
            test_module = getattr(src, self.year)
            solver = getattr(test_module.Solution, func_name)
            return_type = self.return_type(user_func)
            solver_return = self.return_type(solver)

            if return_type != solver_return:
                raise TypeError(f"Mismatched return type expected: {solver_return}, got: {return_type}")

            if not 1 <= num_test_cases <= 1_000_000:
                logging.warning(f"Invalid number of tests cases: {num_test_cases}")
                raise MemoryError("Number of tests cases must be between 1 and 1,000,000")

            test_cases_params = getattr(test_module.Generator, f"{func_name}_test_cases")(num_test_cases)

            # Use multiprocessing to run the tests with a timeout
            result_queue = Queue()
            process = Process(
                target=self._run_test_case,
                kwargs={
                    "user_func": user_func,
                    "solver": solver,
                    "test_cases_params": test_cases_params,
                    "num_test_cases": num_test_cases,
                    "return_type": return_type,
                    "result_queue": result_queue,
                    "show_table": show_table,
                    "more_detail": more_detail
                }
            )

            process.start()
            process.join(timeout=self.runtime_limit)

            if process.is_alive():
                process.terminate()
                process.join()
                raise TimeoutError(f"Function {func_name} timed out after {self.runtime_limit} seconds.")

            formatted_summary_data = result_queue.get()
            self.__handle_log_option(formatted_summary_data)

        except AttributeError as e:
            raise AttributeError(f"Invalid function name: {user_func.__name__}") from e

        except ValueError as e:
            raise ValueError(f"Invalid option: {e}") from e

        except TypeError as e:
            raise TypeError(f"Invalid return type: {e}") from e

        except MemoryError as e:
            raise MemoryError(f"Invalid number of tests cases: {num_test_cases}") from e

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
    def capture_printed_text(
            cls, func: Callable, *args: Iterable
    ) -> Dict[str, Any]:
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
            result = func(*args)

        # Get the captured printed text
        printed_text: str = buffer.getvalue()

        return {
            "result": result,
            "printed_text": printed_text
        }

    def _run_test_case(self: "Tester", **kwargs: Iterable) -> None:
        """
        Run tests cases and compare function outputs.

        Args:
            **kwargs (Dict): Keyword arguments containing the necessary parameters for running the tests:

            :param user_func: Callable, the user-defined function to be tested.
            :param solver: Callable, the solution function to be tested against.
            :param test_cases_params: Iterable, the parameters for the tests cases.
            :param num_test_cases: int, the number of tests cases to generate and run.
            :param return_type: str, the return type of the functions being tested.
            :param result_queue: Queue, the queue to store the tests results.
            :param show_table: bool, whether to show the table of failed cases.

        Returns:
            None

        Note:
            This method runs tests cases using the provided user_func and solver.
            It compares the outputs of these functions, tracks failures, and calculates tests results.

        Raises:
            TimeoutError: If the function execution exceeds the timeout.
            Exception: If an error occurs while generating the summary.
        """

        # Extract keyword arguments for better readability
        user_func: Callable = kwargs["user_func"]
        solver: Callable = kwargs["solver"]
        test_cases_params: Iterable = kwargs["test_cases_params"]
        num_test_cases: int = kwargs["num_test_cases"]
        return_type: str = kwargs["return_type"]
        result_queue: Queue = kwargs["result_queue"]
        show_table: bool = kwargs["show_table"]

        start_time = time.time()

        passed_count = 0
        failed_count = 0
        failed_cases = []

        for params in tqdm(test_cases_params, desc="Running tests cases", unit="tests", disable=self.debug):
            try:
                user_output = self.__caller(user_func, return_type, *params)
                solver_output = self.__caller(solver, return_type, *params)

                if user_output == solver_output:
                    passed_count += 1
                else:
                    failed_count += 1
                    failed_cases.append({
                        "input": params,
                        "expected": solver_output,
                        "result": user_output
                    })

            except TimeoutError:
                failed_count += 1
                failed_cases.append({
                    "input": params,
                    "expected": "Timeout",
                    "result": "Timeout"
                })

            except Exception as e:
                failed_count += 1
                failed_cases.append({
                    "input": params,
                    "expected": "Error",
                    "result": f"Error: {e}"
                })

        end_time = time.time()
        total_time = end_time - start_time

        summary = self.__generate_summary({
            "passed_count": passed_count,
            "failed_count": failed_count,
            "failed_cases": failed_cases,
            "success_rate": (passed_count / num_test_cases) * 100,
            "total_time_result": total_time,
            "average_time": total_time / num_test_cases,
            "test_per_second": num_test_cases / total_time

        }, kwargs["more_detail"], show_table)

        result_queue.put(summary)

    @staticmethod
    def __generate_summary(
            summary_data: Dict, more_detail: bool = False, show_table: bool = False
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
                for case in summary_data["failed_cases"][0:3]:
                    table.append([case["input"], f'{case["expected"]}'[:10], case["result"]][:10])
            else:
                table = [["", "", ""]]

            failed_cases_table = tabulate(table, headers=headers, tablefmt="grid") if show_table else ""

            additional_failed_cases_info = ""
            if show_table and len(summary_data["failed_cases"]) > 3:
                additional_failed_cases_info = f"\nand more...{len(summary_data['failed_cases']) - 3} cases failed"

            summary_kwargs = {
                key: value for key, value in summary_data.items() if key != "failed_cases"
            }

            if more_detail:
                summary = template.more_info.format(
                    failed_cases_table=failed_cases_table,
                    more_info="Table is disabled" if not show_table else additional_failed_cases_info,
                    **summary_kwargs
                )
            else:
                summary = template.simple.format(**summary_kwargs)


        except FileNotFoundError as e:
            print(f"Error: {e}")
            print(f"Error at line {e.__traceback__.tb_lineno}")
            raise FileNotFoundError("Template file not found. Please make sure that the template file exists.") from e

        return summary

    def __handle_log_option(
            self: "Tester", formatted_summary_data: str
    ) -> None:
        """
        Handle the logging option for the tests summary.

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

    @classmethod
    def __caller(
            cls: "Tester",
            func: Callable,
            return_type: str,
            *args: Iterable
    ) -> Any:
        """
        Execute the specified function and capture the output.

        Args:
            func (Callable): The function to be executed.
            *args (Iterable): The arguments to pass to the function.

        Returns:
            str: The output of the function, captured as a string.
        """
        captured_output = cls.capture_printed_text(func, *args)

        if return_type == 'None':
            return captured_output["printed_text"]

        return captured_output["result"]

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
