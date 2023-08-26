import unittest

from corner_frame import corner_frame


class TestCornerFrame(unittest.TestCase):
    def test_corner_frame_with_1(self):
        result = corner_frame(1)
        expected = "1\n"
        self.assertEqual(result, expected)

    def test_corner_frame_with_3(self):
        result = corner_frame(3)
        expected = "1 2 3\n2 2 3\n3 3 3\n"
        self.assertEqual(result, expected)

    def test_corner_frame_with_5(self):
        result = corner_frame(5)
        expected = "1 2 3 4 5\n2 2 3 4 5\n3 3 3 4 5\n4 4 4 4 5\n5 5 5 5 5\n"
        self.assertEqual(result, expected)

    def test_corner_frame_with_negative_input(self):
        # Test with a negative input
        result = corner_frame(-5)
        expected = "\n"
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
