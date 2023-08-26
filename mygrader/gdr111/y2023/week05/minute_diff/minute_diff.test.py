import unittest

from minute_diff import minute_diff


class MinuteDiffTestCase(unittest.TestCase):
    def test_minute_diff_same_period(self):
        # Test case 1: Same time, same period
        self.assertEqual(minute_diff(8, 23, 'AM', 8, 23, 'AM'), 0)
        # Test case 2: Same time, PM period
        self.assertEqual(minute_diff(12, 0, 'PM', 12, 0, 'PM'), 0)
        # Test case 3: Same time, AM period
        self.assertEqual(minute_diff(12, 0, 'AM', 12, 0, 'AM'), 0)

    def test_minute_diff_different_period(self):
        # Test case 4: AM to PM
        self.assertEqual(minute_diff(8, 23, 'AM', 1, 24, 'PM'), 301)
        # Test case 5: PM to AM
        self.assertEqual(minute_diff(1, 24, 'PM', 8, 23, 'AM'), 301)
        # Test case 6: AM to PM (12-hour difference)
        self.assertEqual(minute_diff(12, 0, 'AM', 12, 0, 'PM'), 12 * 60)
        # Test case 7: PM to AM (12-hour difference)
        self.assertEqual(minute_diff(12, 0, 'PM', 12, 0, 'AM'), 12 * 60)

    def test_minute_diff_edge_cases(self):
        # Test case 8: Difference within an hour
        self.assertEqual(minute_diff(12, 10, 'AM', 12, 45, 'AM'), 35)
        # Test case 9: Difference of 12 hours
        self.assertEqual(minute_diff(12, 0, 'AM', 12, 0, 'PM'), 12 * 60)
        # Test case 10: Difference of 0 hours
        self.assertEqual(minute_diff(12, 0, 'AM', 12, 0, 'AM'), 0)


if __name__ == "__main__":
    unittest.main()
