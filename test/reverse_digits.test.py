import unittest
import random

from src.mygrader import print_test_results


def reverse_digits(number: int, reversed_number: int = 0) -> int:
    # Base case: when the number becomes 0, return the reversed_number
    if number == 0:
        return reversed_number

    # Extract the last digit of the number
    last_digit = abs(number) % 10

    # Append the last digit to the reversed_number and remove it from the original number
    reversed_number = reversed_number * 10 + last_digit

    # Recursive call with the remaining number
    return reverse_digits(abs(number) // 10, reversed_number) * (-1 if number < 0 else 1)


# Create a test class that inherits from unittest.TestCase
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

        print_test_results(num_passed, num_failed, failed_cases, True)


if __name__ == "__main__":
    unittest.main()
