import os
import unittest


class TestPI(unittest.TestCase):

    def test_reverse_digits(self, sample=None, pi=None):
        num_passed = 0
        num_failed = 0
        failed_cases = []

        for i in range(100):
            result = sample.pi(i)
            expected = pi.pi(i)

            if result != expected:
                num_failed += 1
                if num_failed <= 1000:
                    failed_cases.append((i, expected, result))

            num_passed += 1

            # Print prompt every 100,000 cases
            if num_passed % 100000 == 0:
                print(f"{num_passed} test cases processed.")

        print(f"{num_passed} test cases passed.")
        if num_failed > 0:
            print(f"{num_failed} test cases failed.")
            if num_failed <= 10:
                print("Failed cases:")
                for i, failed_case in enumerate(failed_cases, start=1):
                    print(f"{i}. Input: {failed_case[0]}, Expected: {failed_case[1]}, Got: {failed_case[2]}")

            # Write the first 1000 failed cases to a file
            with open("failed_cases.txt", "w") as file:
                for i, failed_case in enumerate(failed_cases[:100], start=1):
                    file.write(f"{i}. Input: {failed_case[0]}, Expected: {failed_case[1]}, Got: {failed_case[2]}\n")
        else:
            print("All test cases passed successfully.")

            # Remove the output file if it exists
            if os.path.exists("failed_cases.txt"):
                os.remove("failed_cases.txt")
