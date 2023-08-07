import unittest
import random

from src.mygrader import print_test_results, write_failed_cases_to_file



# Create a test class that inherits from unittest.TestCase
def reverse_digits(num):
    pass


class TestReverseDigits(unittest.TestCase):

    def test_reverse_digits(self):
        num_test_cases = 1_000_000
        num_passed = 0
        num_failed = 0
        failed_cases = []

        for i in range(num_test_cases):
            num = random.randint(-10 ** 9, 10 ** 9)  # Random integer between -10^9 and 10^9
            reversed_num = reverse_digits(num)
            expected_reversed_num = int(str(abs(num))[::-1]) * (-1 if num < 0 else 1)

            # Check if reversed_num matches the expected_reversed_num
            if reversed_num != expected_reversed_num:
                num_failed += 1
                if num_failed <= 1000:
                    failed_cases.append((num, expected_reversed_num, reversed_num))

            num_passed += 1

            # Print prompt every 100,000 cases
            if num_passed % 100000 == 0:
                print(f"{num_passed} test cases processed.")

        failed_cases = print_test_results(num_passed, num_failed, failed_cases)
        write_failed_cases_to_file(failed_cases)


if __name__ == "__main__":
    unittest.main()
