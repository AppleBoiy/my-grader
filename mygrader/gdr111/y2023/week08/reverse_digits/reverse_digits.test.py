import random
import unittest

from mygrader import print_test_results

from reverse_digits_v3 import reverse_digits


def rev(num):
    ans = int(str(abs(num))[::-1])
    if num < 0:
        ans *= -1
    return ans


class TestReverseDigits(unittest.TestCase):

    def test_reverse_digits(self):
        num_test_cases = 1_000_000
        num_passed = 0
        num_failed = 0
        failed_cases = []

        for i in range(num_test_cases):
            num = random.randint(-10 ** 9, 10 ** 9)  # Random integer between -10^9 and 10^9
            result = reverse_digits(num)
            expected = rev(num)

            # Check if a result matches the expected
            if result != expected:
                num_failed += 1
                if num_failed <= 1000:
                    failed_cases.append((num, expected, result))
            else:
                num_passed += 1

            # Print progress every 100,000 cases
            if (i + 1) % 100000 == 0:
                print(f"P: {i + 1:_} out of {num_test_cases:_} test cases passed.")

        # Print overall test results
        print_test_results(num_passed, num_failed, failed_cases, True)


if __name__ == "__main__":
    unittest.main()
