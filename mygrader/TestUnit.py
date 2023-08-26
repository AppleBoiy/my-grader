import random
import time
import unittest
from typing import List, Callable

from timeout_decorator import timeout
from tqdm import tqdm

from mygrader.gdr111.y2023.week02 import Solution


class TimeoutTestResult(unittest.TextTestResult):
    def __init__(self, *args, max_execution_time=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.max_execution_time = max_execution_time
        self.start_time = time.time()
        self.test_start_time = None  # Initialize test_start_time

    def startTest(self, test):
        super().startTest(test)
        self.test_start_time = time.time()  # Record test start time

    def stopTest(self, test):
        elapsed_time = time.time() - self.start_time
        if self.max_execution_time and elapsed_time > self.max_execution_time:
            self.addError(test, f"Test execution time exceeded {self.max_execution_time} seconds")
        super().stopTest(test)


class Test(Solution, unittest.TestCase):

    def __int__(self, *args, **kwargs):
        super().__init__()

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

    @classmethod
    def generate_test_cases(cls, num_test_cases: int) -> List:
        """
        Generate a list of test cases with random parameters.

        Args:
            num_test_cases (int): Number of test cases to generate.

        Returns:
            List[Dict[str, int]]: List of dictionaries containing test options for each case.
        """
        test_cases = []
        for _ in range(num_test_cases):
            x = random.randint(1, 10 ** 9)  # Generate random x value
            y = random.randint(x, 10 ** 9)  # Generate random y value
            test_cases.append((x, y))
        return test_cases

    @classmethod
    @timeout(10)  # Set the maximum execution time to 10 seconds
    def run_test(
            cls,
            test_function_name: str,
            num_test_cases: int,
            options: str,
            compare_user_function: Callable
    ) -> None:
        """
        Run tests for the specified function using generated test cases.

        Args:
            test_function_name (str): Name of the function to test.
            num_test_cases (int): Number of test cases to generate and run.
            options (str): Output options ("print", "file", "none").
            compare_user_function (Callable[[int, int], int]): User-defined function to compare output with Solution function.
        """
        passed_count = 0
        failed_count = 0

        custom_test_instance = cls()

        test_cases_params = custom_test_instance.generate_test_cases(num_test_cases)

        for i in tqdm(range(num_test_cases), desc="Running tests", unit="test"):

            expected = getattr(custom_test_instance, test_function_name)(*test_cases_params[i])
            result = compare_user_function(*test_cases_params[i])

            if expected == result:
                passed_count += 1
            else:
                failed_count += 1
        print("\nTest summary:")
        print(f"Passed: {passed_count}/{num_test_cases}")
        print(f"Failed: {failed_count}/{num_test_cases}")
