import contextlib
import inspect
import io
import sys
import time
import unittest
from typing import Callable, Dict, Iterable

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
            self, year: int, runtime_limit: float = 1.0, log_option: str = 'print', debug: bool = False
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
        self.year = f'y{year}'
        self.runtime_limit = runtime_limit
        self.log_option = log_option
        self.debug = debug

    @classmethod
    def __generate_markdown_summary(
            cls, summary_data: Dict, show_table: bool = False
    ) -> str:
        """
        Generate a markdown summary based on the provided summary data and template.

        Args:
            summary_data (Dict): Dictionary containing summary data.
            show_table (bool): Whether to show the table of failed cases.

        Returns:
            str: The formatted markdown summary.
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
                passed_count=summary_data["passed_count"],
                failed_count=summary_data["failed_count"],
                success_rate=summary_data["success_rate"],
                average_time=summary_data["average_time"],
                total_time_result=summary_data["total_time_result"],
                test_per_second=summary_data["test_per_second"],
                more_info="Table is disabled" if not show_table else "",
            )
        except FileNotFoundError as e:
            print(f"Error: {e}")
            print(f"Error at line {e.__traceback__.tb_lineno}")
            raise FileNotFoundError("Template file not found. Please make sure that the template file exists.")

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
            return_type = self.__return_type__(solver)

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
                    "failed_cases": _failed_cases,
                    "test_per_second": num_test_cases / _total_time,
                    "success_rate": (_passed_count / num_test_cases) * 100,

                }

            # TODO: More options for logging, e.g., JSON, CSV, etc.
            try:
                result = run_test_case()

            except TimeoutError:
                raise TimeoutError(f"Runtime limit exceeded for when run test cases for {func_name}().")

            summary_data = {
                "failed_cases": result["failed_cases"][0:10],
                "passed_count": result["passed_count"],
                "failed_count": result["failed_count"],
                "success_rate": result["success_rate"],
                "average_time": result["average_time"],
                "total_time_result": result["total_time_result"],
                "test_per_second": result["test_per_second"],
            }

            formatted_summary_data = self.__generate_markdown_summary(summary_data, show_table)

            if self.log_option == "print":
                print(formatted_summary_data)
            elif self.log_option == "write":
                with open("test_summary.md", "w") as f:
                    f.write(formatted_summary_data)
            elif self.log_option == "None":
                return
            else:
                raise ValueError(f"Invalid option: {self.log_option}")

        except (ValueError, FileNotFoundError) as e:
            print(f"Error: {e}")
            if self.debug:
                print(f"Error at line {e.__traceback__.tb_lineno}")

        except AttributeError:
            info = sys.exc_info()
            raise AttributeError(f"Invalid function name: {user_func.__name__}") from info[1]

        except Exception as e:
            if self.debug:
                print(f"Error at line {e.__traceback__.tb_lineno}: ", e)
            print("An error occurred while running the test.")

    @classmethod
    def __return_type__(cls, func: Callable) -> str:
        """
        Return the return type of the given function.

        Args:
            func (Callable): The function to be tested.

        Returns:
            str: The return type of the given function.
        """
        signature = inspect.signature(func)
        return_annotation = signature.return_annotation

        return str(return_annotation)

    @classmethod
    def capture_printed_text(cls, func: Callable, *args) -> str:
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
        printed_text = buffer.getvalue()

        return printed_text

    def __dir__(self) -> Iterable[str]:
        """
        Return the list of available functions for the given year.

        Returns:
            Iterable[str]: List of available functions.
        """
        return [func for func in dir(getattr(src, self.year)) if not func.startswith("__")]

    def __repr__(self) -> str:
        """
        Return the list of available functions for the given year.

        Returns:
            str: List of available functions.
        """
        return f"Available functions for {self.year}: {self.__dir__()}"

    def __str__(self) -> str:
        # TODO: Add more information
        return f"Tester class for the year {self.year}"
