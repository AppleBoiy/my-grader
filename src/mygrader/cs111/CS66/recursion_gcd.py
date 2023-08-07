import os
import unittest
import random
from math import gcd



class TestGCDFunction(unittest.TestCase):
    def test_gcd_random_numbers(self, recursion_gcd=None):
        failed_cases = []

        for i in range(1_000_000):
            x = random.randint(1, 10 ** 9)
            y = random.randint(1, 10 ** 9)
            try:
                self.assertEqual(gcd(x, y), recursion_gcd.gcd(x, y))
            except AssertionError as e:
                failed_cases.append((x, y, e))
            if (i + 1) % 100_000 == 0:
                print(f'{i + 1} test cases passed.')

        num_failures = len(failed_cases)
        if num_failures > 0:
            print(f"\nNumber of test cases failed: {num_failures}")
            with open("failed_cases.txt", "w") as file:
                print("\nTest cases that failed:")
                for i, case in enumerate(failed_cases):
                    x, y, error = case

                    if i > 100:
                        break
                    file.write(f"gcd({x}, {y}) -> Expected: {gcd(x, y)}, Actual: {recursion_gcd.gcd(x, y)}\n")
        else:
            print("All test cases passed successfully.")
            # Remove the output file if it exists
            if os.path.exists("failed_cases.txt"):
                os.remove("failed_cases.txt")



if __name__ == '__main__':
    unittest.main(exit=False)
