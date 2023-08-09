import unittest

from num2words import num2words
from numpy import random
from mygrader import print_test_results

from mygrader.sample import num_to_word


class TestNumberToWords(unittest.TestCase):

    def test_zero(self):
        self.assertEqual(num_to_word(0), "zero")

    def test_single_digits(self):
        for num in range(1, 10):
            expected_word = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"][num - 1]
            self.assertEqual(num_to_word(num), expected_word)

    def test_two_digits(self):
        test_cases = {
            10: "ten",
            11: "eleven",
            12: "twelve",
            13: "thirteen",
            14: "fourteen",
            15: "fifteen",
            16: "sixteen",
            17: "seventeen",
            18: "eighteen",
            19: "nineteen",
            20: "twenty",
            21: "twenty-one",
            30: "thirty",
            50: "fifty",
            80: "eighty",
            99: "ninety-nine",
        }

        for num, expected_word in test_cases.items():
            self.assertEqual(num_to_word(num), expected_word)

    def test_three_digits(self):
        test_cases = {
            100: "one hundred",
            205: "two hundred five",
            999: "nine hundred ninety-nine",
            300: "three hundred",
            850: "eight hundred fifty",
            666: "six hundred sixty-six",
            700: "seven hundred",
        }

        for num, expected_word in test_cases.items():
            self.assertEqual(num_to_word(num), expected_word)

    def test_millions(self):
        test_cases = {
            1_000_000: "one million",
            123_456_789: "one hundred twenty-three million "
                         "four hundred fifty-six thousand "
                         "seven hundred eighty-nine",
            1_000_000_000: "one billion",
            987_654_321: "nine hundred eighty-seven million "
                         "six hundred fifty-four thousand "
                         "three hundred twenty-one",
            2_000_000_000: "two billion",
        }

        for num, expected_word in test_cases.items():
            self.assertEqual(num_to_word(num), expected_word)

        for num, expected_word in test_cases.items():
            self.assertEqual(num_to_word(num), expected_word)

    # def test_invalid_input(self):
    #     # Test cases for invalid inputs
    #     with self.assertRaises(ValueError):
    #         num_to_word(-123)
    #     with self.assertRaises(ValueError):
    #         num_to_word(1_234_567_890_123_456_789)

    def test_large_input(self):
        # Test cases for the largest possible input within the valid range
        expected_word = (
            "nine hundred ninety-nine billion "
            "nine hundred ninety-nine million "
            "nine hundred ninety-nine thousand "
            "nine hundred ninety-nine"
        )
        self.assertEqual(num_to_word(999_999_999_999), expected_word)

    def test_random_numbers(self):
        # Generate 10000 random numbers between 0 and 999_999_999_999

        num_passed = 0
        num_failed = 0
        failed_cases = []

        for i in range(100000):
            num = random.randint(0, 999_999_999_999)

            # Convert the number using the function under test
            converted = ""
            try:
                converted = num_to_word(num)
            except IndexError as err:
                ...

            # Generate the expected word representation
            expected = (
                num2words(num)
                .replace(',', '')
                .replace('and ', '')
                .replace('and', '')
                .replace('thous ', 'thousand ')
                .replace('thous', 'thousand ')
                .strip()
            )

            # Check if reversed_num matches the expected_reversed_num
            if converted != expected:
                num_failed += 1
                if num_failed <= 1000:
                    failed_cases.append((num, expected, converted))

            num_passed += 1

            # Print prompt every 100,000 cases
            if num_passed % 10000 == 0:
                print(f"{num_passed} test cases processed.")

        print_test_results(num_passed, num_failed, failed_cases)


if __name__ == '__main__':
    unittest.main()
