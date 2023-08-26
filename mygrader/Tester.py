import sys
import time
import unittest
from typing import Callable, Dict

from tabulate import tabulate
from timeout_decorator import timeout
from tqdm import tqdm

from mygrader import Solution
from mygrader.template import template


class Tester(unittest.TestCase):
    """
    A test class to run tests on user-defined functions.

    Attributes:
        year (str): The year for which the tests are being run (e.g., "y2023").
        runtime_limit (float): The maximum runtime allowed for a function.
        log_option (str): The logging option ("print" or "write") for the test summary.
    """

    def __init__(self, year: int, runtime_limit: float = 1.0, log_option: str = 'print') -> None:
        """
        Initialize the Tester class.

        Args:
            year (int): The year for which the tests are being run (e.g., 2023).
            runtime_limit (float): The maximum runtime allowed for a function.
            log_option (str): The logging option ("print" or "write") for the test summary.
        """
        super().__init__()
        self.year = f'y{year}'
        self.runtime_limit = runtime_limit
        self.log_option = log_option

    @classmethod
    def generate_markdown_summary(
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
            num_test_cases: int = 1_000_000,
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
            function with the expected output from the Solution class and calculates
            the success rate. The test results can be printed or written to a file
            based on the provided options.

        Example:
            >>> from mygrader.Tester import Tester

            >>> # Create a Test object (runtime_limit is optional)
            >>> opt = "print" # Output options ("print" or "write")
            >>> tester = Tester(runtime_limit=4, log_option=opt)
            >>> func = lambda x: x + 1 # User-defined function to be tested

            >>> tester.run_test(2023, func)

        """

        # TODO: Add support for multiple functions
        try:
            test_module = getattr(Solution, self.year)

            test_cases_params = getattr(test_module.Generator, f"{user_func.__name__}_test_cases")(num_test_cases)

        except AttributeError:
            info = sys.exc_info()
            raise AttributeError(f"Invalid function name: {user_func.__name__}") from info[1]

        print(f'Testing... {user_func.__name__}() with {num_test_cases} test cases.')

        @timeout(self.runtime_limit)
        def run_test_case():
            start_time = time.time()
            _passed_count = 0
            _failed_count = 0
            _failed_cases = []

            for case in tqdm(range(num_test_cases), desc="Running tests", unit="test"):
                _input = test_cases_params[case]

                _expected = getattr(test_module.Solution, user_func.__name__)(*_input)
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

            summary_data = {
                "failed_cases": result["failed_cases"][0:10],
                "passed_count": result["passed_count"],
                "failed_count": result["failed_count"],
                "success_rate": result["success_rate"],
                "average_time": result["average_time"],
                "total_time_result": result["total_time_result"],
                "test_per_second": result["test_per_second"],
            }

            formatted_summary_data = self.generate_markdown_summary(summary_data, show_table)

            if self.log_option == "print":
                print(formatted_summary_data)
            elif self.log_option == "write":
                with open("test_summary.md", "w") as f:
                    f.write(formatted_summary_data)
            else:
                raise ValueError(f"Invalid option: {self.log_option}")

        except (ValueError, FileNotFoundError) as e:
            print(f"Error: {e}")
            print(f"Error at line {e.__traceback__.tb_lineno}")

        except Exception as e:
            print(f"Error at line {e.__traceback__.tb_lineno}: ", e)
            print("An error occurred while running the test.")
