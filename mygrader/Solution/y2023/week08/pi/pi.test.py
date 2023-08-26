import unittest

from mygrader import print_test_results

import pi_v1
import pi_v2


class TestPI(unittest.TestCase):

    def test_reverse_digits(self):

        num_passed = 0
        num_failed = 0
        failed_cases = []

        for i in range(100):
            result = pi_v2.pi(i)
            expected = pi_v1.pi(i)

            if result != expected:
                num_failed += 1
                if num_failed <= 1000:
                    failed_cases.append((i, expected, result))

            num_passed += 1

        print_test_results(num_passed, num_failed, failed_cases, True)


if __name__ == '__main__':
    unittest.main()
