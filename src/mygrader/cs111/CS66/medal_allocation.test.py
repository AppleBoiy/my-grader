import unittest


def medal_allocation(param):
    pass


class TestMedalAllocation(unittest.TestCase):
    def test_empty_list(self):
        result = medal_allocation([])

        self.assertEqual(result, ([], [], []), "Empty list should return empty lists for all medals")

    def test_one_gold_medalist(self):
        result = medal_allocation([5])
        self.assertEqual(result, ([5], [], []), "One gold medalist should have no silver or bronze medalists")

    def test_one_silver_medalist(self):
        result = medal_allocation([5, 3])
        self.assertEqual(result, ([5], [3], []), "One silver medalist should have no bronze medalists")

    def test_two_silver_medalists(self):
        result = medal_allocation([5, 7, 8, 2, 7, 1])
        self.assertEqual(result, ([8], [7, 7], []), "Two silver medalists should have no bronze medalists")

    def test_three_or_more_gold_medalists(self):
        result = medal_allocation([5, 9, 9, 2, 7, 9, 6])
        self.assertEqual(result, ([9, 9, 9], [], []),
                         "Three or more gold medalists should have no silver or bronze medalists")

    def test_custom_cases(self):
        # Additional test cases
        result = medal_allocation([9, 8, 7, 6, 5, 4, 3, 2])
        self.assertEqual(result, ([9], [8], [7]), "Case [9, 8, 7, 6, 5, 4, 3, 2] should be handled correctly")

        result = medal_allocation([9, 8, 7, 7, 6, 5, 4, 3, 2])
        self.assertEqual(result, ([9], [8], [7, 7]), "Case [9, 8, 7, 7, 6, 5, 4, 3, 2] should be handled correctly")

        result = medal_allocation([9, 9, 8, 7, 6, 5, 4, 3, 2])
        self.assertEqual(result, ([9, 9], [], [8]), "Case [9, 9, 8, 7, 6, 5, 4, 3, 2] should be handled correctly")

        result = medal_allocation([9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2])
        self.assertEqual(result, ([9, 9, 9, 9], [], []),
                         "Case [9, 9, 9, 9, 8, 7, 6, 5, 4, 3, 2] should be handled correctly")


if __name__ == '__main__':
    unittest.main()
