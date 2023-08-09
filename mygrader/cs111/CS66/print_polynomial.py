import unittest


from mygrader.sample import print_polynomial


class TestPolynomialFunctions(unittest.TestCase):

    def setUp(self):
        # Common data setup for multiple test cases
        self.polynomial_1 = [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1)]
        self.polynomial_2 = [(1, 2), (0, -10), (14, -7), (1, 0)]
        self.polynomial_3 = [(1, 0), (2, 0), (3, 0), (4, 0), (5, 0)]
        self.polynomial_4 = [(2, -6), (0, -8), (1, 34)]

    def test_print_polynomial_with_z_variable(self):
        # Test print_polynomial with 'z' variable
        self.assertEqual(print_polynomial(self.polynomial_1, 'z'), 'z^5 + z^4 + z^3 + z^2 + z')

    def test_print_polynomial_with_x_variable(self):
        # Test print_polynomial with 'x' variable
        self.assertEqual(print_polynomial(self.polynomial_2, 'x'), '-7x^14 + 2x - 10')
        self.assertEqual(print_polynomial(self.polynomial_4, 'x'), '-6x^2 + 34x - 8')

    def test_print_polynomial_with_a_variable(self):
        # Test print_polynomial with 'a' variable
        self.assertEqual(print_polynomial(self.polynomial_3, 'a'), '0')

    def test_print_polynomial_with_y_variable(self):
        # Test print_polynomial with 'y' variable
        self.assertEqual(print_polynomial(self.polynomial_4, 'y'), '-6y^2 + 34y - 8')

    def test_print_polynomial_single_term(self):
        # Test print_polynomial with a single term
        self.assertEqual(print_polynomial([(1, 2)], 'x'), '2x')
        self.assertEqual(print_polynomial([(0, 0)], 'x'), '0')


if __name__ == '__main__':
    unittest.main()
