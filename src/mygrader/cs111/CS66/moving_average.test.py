import unittest


def moving_average(data_points, window_size):
    pass


class TestMovingAverages(unittest.TestCase):

    def test_moving_averages(self):
        data_points = [1, 2, 3, 4, 5, 6]
        window_size = 3

        # Test without a debug mode
        expected_result = [2.0, 3.0, 4.0, 5.0]
        self.assertEqual(moving_average(data_points, window_size), expected_result)

        # Test with small data points and window size
        data_points = [1, 2, 3]
        window_size = 2
        expected_result = [1.5, 2.5]
        self.assertEqual(moving_average(data_points, window_size), expected_result)

        # Test with a window size equal to the data points' length
        data_points = [1, 2, 3, 4]
        window_size = 4
        expected_result = [2.5]
        self.assertEqual(moving_average(data_points, window_size), expected_result)

        # Test with negative data points
        data_points = [-1, -2, -3, -4, -5]
        window_size = 3
        expected_result = [-2.0, -3.0, -4.0]
        self.assertEqual(moving_average(data_points, window_size), expected_result)

        # Test with floating-point data points
        data_points = [0.5, 1.5, 2.5, 3.5, 4.5]
        window_size = 4
        expected_result = [2.0, 3.0]
        self.assertEqual(moving_average(data_points, window_size), expected_result)

        # Test with an empty data_points list
        data_points = []
        window_size = 3
        expected_result = []
        self.assertEqual(moving_average(data_points, window_size), expected_result)

        # Test with a window size larger than the data points' length
        data_points = [1, 2, 3, 4, 5]
        window_size = 6
        expected_result = []
        self.assertEqual(moving_average(data_points, window_size), expected_result)


if __name__ == '__main__':
    unittest.main()
