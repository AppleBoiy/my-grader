import unittest


def triangle(num_rows):
    pass


class TestTriangle(unittest.TestCase):

    def test_triangle_with_three_rows(self):
        # Test triangle with three rows
        num_rows = 3
        expected_output = "* \n*.*\n* * * \n"
        self.assertEqual(triangle(num_rows), expected_output)


    def test_triangle(self):
        T3 = '''*
    *.*
    * * *
    '''

        T7 = '''*
    *.*
    *...*
    *.....*
    *.......*
    *.........*
    * * * * * * *
    '''

        assert triangle(3) == T3
        assert triangle(7) == T7
        print("OK")


if __name__ == '__main__':
    unittest.main()
