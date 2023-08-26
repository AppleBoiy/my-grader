import random
from typing import List


class Generator:

    @classmethod
    def calculate_sum_test_cases(cls, num_test_cases: int) -> List:
        """
        Generate a list of test cases with random parameters.

        Args:
            num_test_cases (int): Number of test cases to generate.
        """
        test_cases = []
        for _ in range(num_test_cases):
            x = random.randint(1, 10 ** 9)  # Generate random x value
            y = random.randint(x, 10 ** 9)  # Generate random y value
            test_cases.append((x, y))
        return test_cases

    @classmethod
    def calculate_new_price_test_cases(cls, num_test_cases: int) -> List:
        """
        Generate a list of test cases with random parameters.

        Args:
            num_test_cases (int): Number of test cases to generate.
        """
        test_cases = []
        for _ in range(num_test_cases):
            old_price = random.uniform(0.0, 1000.0)  # Generate random old price between 0 and 1000
            test_cases.append((old_price,))
        return test_cases

    @classmethod
    def calculate_triangle_area_test_cases(cls, num_test_cases: int) -> List:
        """
        Generate a list of test cases with random parameters.

        Args:
            num_test_cases (int): Number of test cases to generate.
        """
        test_cases = []
        for _ in range(num_test_cases):
            a = random.uniform(0.0, 1000.0)
            b = random.uniform(0.0, 1000.0)
            c = random.uniform(0.0, 1000.0)
            test_cases.append((a, b, c))
        return test_cases
