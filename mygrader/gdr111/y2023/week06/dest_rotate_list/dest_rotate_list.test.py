import unittest

from week06.dest_rotate_list.dest_rotate_list import dest_rotate_list


class TestRotateList(unittest.TestCase):

    def test_rotate_list_by_zero(self):
        # Test rotating by zero should not change the list
        my_list = [1, 2, 3, 4, 5]
        rotate_by = 0
        dest_rotate_list(my_list, rotate_by)
        self.assertEqual(my_list, [1, 2, 3, 4, 5])

    def test_rotate_list_by_positive(self):
        # Test rotating by a positive number
        my_list = [1, 2, 3, 4, 5]
        rotate_by = 2
        dest_rotate_list(my_list, rotate_by)
        self.assertEqual(my_list, [4, 5, 1, 2, 3])

    def test_rotate_list_by_negative(self):
        # Test rotating by a negative number
        my_list = [1, 2, 3, 4, 5]
        rotate_by = -1
        dest_rotate_list(my_list, rotate_by)
        self.assertEqual(my_list, [2, 3, 4, 5, 1])

    def test_rotate_list_by_large_number(self):
        # Test rotating by a large number (greater than the list length)
        my_list = [1, 2, 3, 4, 5]
        rotate_by = 8
        dest_rotate_list(my_list, rotate_by)
        self.assertEqual(my_list, [3, 4, 5, 1, 2])

    def test_rotate_list_empty_list(self):
        # Test rotating an empty list
        my_list = []
        rotate_by = 3
        dest_rotate_list(my_list, rotate_by)
        self.assertEqual(my_list, [])

    def test_rotate_list_single_element_list(self):
        # Test rotating a single-element list
        my_list = [42]
        rotate_by = 5
        dest_rotate_list(my_list, rotate_by)
        self.assertEqual(my_list, [42])


if __name__ == '__main__':
    unittest.main()
