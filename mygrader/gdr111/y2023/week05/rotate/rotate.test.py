import unittest

from rotate import rotate


class RotateTests(unittest.TestCase):
    def test_rotate_positive_shift(self):
        # Test cases for positive shift values
        self.assertEqual(rotate(12345, 2), 45123)
        self.assertEqual(rotate(987654321, 4), 432198765)

    def test_rotate_negative_shift(self):
        # Test cases for negative shift values
        self.assertEqual(rotate(12345, -2), 34512)
        self.assertEqual(rotate(987654321, -4), 543219876)

    def test_rotate_zero_shift(self):
        # Test case for zero shift value
        self.assertEqual(rotate(12345, 0), 12345)
        self.assertEqual(rotate(987654321, 0), 987654321)

    def test_rotate_large_shift(self):
        # Test cases for shift values larger than the number length
        self.assertEqual(rotate(12345, 7), 45123)
        self.assertEqual(rotate(987654321, 10), 198765432)

    def test_rotate_single_digit_number(self):
        # Test case for single-digit number
        self.assertEqual(rotate(5, 1), 5)
        self.assertEqual(rotate(9, -1), 9)


if __name__ == "__main__":
    unittest.main()
