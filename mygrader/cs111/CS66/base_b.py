import unittest
import random

from mygrader.sample import base_b


class TestConvertBaseTenToBaseB(unittest.TestCase):

    def test_conversion_to_base_b(self):
        # Test the conversion function for various random numbers and bases from 2 to 10
        failed_cases = []
        total_cases = 100000
        prompt_interval = 10000

        for i in range(total_cases):
            number = random.randint(0, 1000000)
            for base in range(2, 11):
                with self.subTest(number=number, base=base):
                    try:
                        # Convert the number to the given base using the conversion function
                        converted_number = base_b(number, base)

                        # Convert the converted number back to base 10 using Python's built-in int() function
                        converted_back = int(str(converted_number), base)

                        # Check if the original number and the converted back number match
                        if number != converted_back:
                            failed_cases.append(
                                (number, base, f"Conversion failed for number {number} to base {base}. "
                                               f"Expected: {number}, Got: {converted_back}")
                            )
                    except ValueError as err:
                        failed_cases.append(
                            (number, base, str(err))
                        )

            # Display prompt after every 10000 successful test cases
            if (i + 1) % prompt_interval == 0:
                print(f"{i + 1} out of {total_cases} test cases passed.")

        # Final prompt with the total number of passed test cases
        print(f"\nTest Results:")
        print(f"Total test cases: {total_cases}")
        print(f"Passed test cases: {total_cases - len(failed_cases)}")
        print(f"Failed test cases: {len(failed_cases)}")

        # Print the details of the failed test cases (limit to 10 for brevity)
        if failed_cases:
            print("\nFailed Test Cases:")
            for number, base, error_msg in failed_cases[:10]:
                print(f"Test case {number} to base {base}: {error_msg}")


if __name__ == "__main__":
    unittest.main(exit=False)
