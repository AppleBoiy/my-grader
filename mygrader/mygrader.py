import contextlib
import inspect
import io
import os
import sys
import time
import unittest
from copy import deepcopy
from math import isclose
from multiprocessing import Process, Queue
from typing import Callable, Dict, Iterable, Any

from tabulate import tabulate
from tqdm import tqdm

from mygrader import src, template


class Tester(unittest.TestCase):

    def __init__(
            self,
            year: int,
            log_option: str = 'print',
            debug: bool = False,
            runtime_limit: int = 1,
            more_detail: bool = False,
            show_table: bool = False
    ) -> None:
        """
        Initialize the Tester class.

        Args:
           year (int): The year for which the tests are being run (e.g., 2023).
           log_option (str): The logging option ("print" or "write") for the tests summary.
           debug (bool): If True, enable debug mode for additional information.
           runtime_limit (int): The maximum runtime limit (in seconds) for each test case execution.
           more_detail (bool): If True, provide more detailed information in the summary.
           show_table (bool): If True, show the table of failed cases in the summary.

        Note:
           The `runtime_limit` parameter defines the maximum time a tests case execution is allowed to take.
           If a test case execution exceeds this limit, it will be terminated and considered as a TimeoutError.
        """
        super().__init__()
        self.year: str = f'y{year}'
        self.log_option: str = log_option
        self.debug: bool = debug
        self.runtime_limit: int = runtime_limit
        self.more_detail: bool = more_detail
        self.show_table: bool = show_table

    def run_test(self, user_func: Callable, num_test_cases: int = 100) -> None:
        """
        Run tests for the specified function using generated test cases.

        Args:
            user_func (Callable): The user-defined function to be tested.
            num_test_cases (int): The number of test cases to generate and run.

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

        try:
            # Get the test module corresponding to the specified year
            test_module = getattr(src, self.year)

            # Get the solver function corresponding to the user function
            solver = getattr(test_module.Solution, user_func.__name__)

            # Get return type information for both the user and solver functions
            return_type = self.return_type(user_func)
            solver_return = self.return_type(solver)

            # Check for mismatched return types
            if return_type["type"] != solver_return["type"]:
                raise TypeError(
                    f"Mismatched return type expected: {solver_return['type']}, got: {return_type['type']}")

            # Check if the function is destructive/non-destructive as expected
            if return_type["is_dest"] != solver_return["is_dest"]:
                expected_property = "destructive" if solver_return["is_dest"] else "non-destructive"
                raise ValueError(f"This function should be {expected_property}, but your function is not.")

            if num_test_cases > 1_000_000:
                raise MemoryError("Too many test cases. Please reduce the number of test cases.")
            if num_test_cases < 1:
                raise ValueError("Invalid number of test cases. Please provide a positive integer.")

            # Generate test case parameters using the Generator class
            test_cases_params = getattr(test_module.Generator, f"{user_func.__name__}_test_cases")(num_test_cases)

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
                    "result_queue": result_queue
                }
            )

            process.start()
            process.join(timeout=self.runtime_limit)

            if process.is_alive():
                process.terminate()
                process.join()
                raise TimeoutError(f"Function {user_func.__name__} timed out after {self.runtime_limit} seconds.")

            formatted_summary_data = result_queue.get()
            self.__handle_log_option(formatted_summary_data)

        except TimeoutError as e:
            raise TimeoutError(f"Function {user_func.__name__} timed out after {self.runtime_limit} seconds.") from e

        except AttributeError as e:
            raise AttributeError(f"Invalid function name: {user_func.__name__}") from e

        except ValueError as e:
            raise ValueError(f"Invalid option: {e}") from e

        except TypeError as e:
            raise TypeError(f"Invalid return type: {e}") from e

        except MemoryError as e:
            raise MemoryError(f"Invalid number of test cases: {num_test_cases}") from e

    @classmethod
    def return_type(cls, func: Callable) -> Dict[str, bool]:
        """
        Obtain the return type and determine if the function is destructive.

        This method accepts a callable function as input and provides a dictionary
        with information about its return type and whether the function is destructive.

        Args:
            func (Callable): The function to be analyzed.

        Returns:
            Dict[str, bool]: A dictionary with 'type' (str) and 'is_dest' (bool).

        Example:
            >>> def add(a: int, b: int) -> int:
            ...     return a + b
            ...
            >>> Tester.return_type(add)
            {'type': 'int', 'is_dest': False}
        """
        original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')  # Redirect stdout to null device

        result = {
            'type': None,
            'is_dest': False
        }

        try:
            signature = inspect.signature(func)
            return_annotation = signature.return_annotation

            generator_method = getattr(src.Generator, f"{func.__name__}_test_cases")
            test_case = generator_method(1)
            original_test_case = deepcopy(test_case)

            if return_annotation is inspect.Signature.empty:
                return_annotation = type(func(*test_case[0]))

            if str(return_annotation) == "<class 'NoneType'>":
                result['type'] = 'None'
            else:
                result['type'] = str(return_annotation)

            if test_case != original_test_case:
                result['is_dest'] = True

        except AttributeError:
            raise AttributeError(f"Function not found in the Generator class: {func.__name__}")

        finally:
            sys.stdout = original_stdout  # Restore original stdout

        return result

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

        Returns:
            None

        Note:
            This method runs test cases using the provided user_func and solver.
            It compares the outputs of these functions, tracks failures, and calculates test results.

        Raises:
            TimeoutError: If the function execution exceeds the timeout.
            Exception: If an error occurs while generating the summary.
        """

        # the user-defined function to be tested.
        user_func: Callable = kwargs["user_func"]
        # the solution function to be tested against.
        solver: Callable = kwargs["solver"]
        # the parameters for the test cases.
        test_cases_params: Iterable = kwargs["test_cases_params"]
        # the number of test cases to generate and run.
        num_test_cases: int = kwargs["num_test_cases"]
        # the return type of the functions being tested.
        return_type: str = kwargs["return_type"]
        # the queue to store the tests results.
        result_queue: Queue = kwargs["result_queue"]

        start_time = time.time()

        passed_count = 0
        failed_count = 0
        failed_cases = []

        for params in tqdm(test_cases_params, desc="Running test cases", unit="tests", disable=self.debug):
            try:
                user_params = deepcopy(params)
                solver_params = deepcopy(params)

                user_output = self.__caller(user_func, return_type, *user_params)
                solver_output = self.__caller(solver, return_type, *solver_params)

                if isinstance(user_output, float) and isclose(user_output, solver_output, rel_tol=1e-9):
                    passed_count += 1
                elif user_output == solver_output:
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

        # Generate and format the summary based on the test results
        summary = self.__generate_summary({
            "passed_count": passed_count,
            "failed_count": failed_count,
            "failed_cases": failed_cases,
            "success_rate": (passed_count / num_test_cases) * 100,
            "total_time_result": total_time,
            "average_time": total_time / num_test_cases,
            "test_per_second": num_test_cases / total_time
        })

        result_queue.put(summary)

    def __generate_summary(self, summary_data: Dict) -> str:
        """
        Generate a summary based on the provided summary data and template.

        Args:
            summary_data (Dict): Dictionary containing summary data.

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

            if self.show_table:
                # If show_table is enabled, populate the table with data from failed cases (up to 3 cases)
                for case in summary_data["failed_cases"][0:3]:
                    table.append([case["input"], f'{case["expected"]}'[:10], case["result"]][:10])
            else:
                # If show_table is disabled, display an empty row
                table = [["", "", ""]]

            # Generate the table format using tabulate (grid format)
            failed_cases_table = tabulate(table, headers=headers, tablefmt="grid") if self.show_table else ""

            # Additional info about more failed cases if applicable
            additional_failed_cases_info = ""
            if self.show_table and len(summary_data["failed_cases"]) > 3:
                additional_failed_cases_info = f"\nand more...{len(summary_data['failed_cases']) - 3} cases failed"

            summary_kwargs = {
                key: value for key, value in summary_data.items() if key != "failed_cases"
            }

            # Generate the summary using the appropriate template based on a more_detail option
            if self.more_detail:
                summary = template.more_info.format(
                    failed_cases_table=failed_cases_table,
                    more_info="Table is disabled" if not self.show_table else additional_failed_cases_info,
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
