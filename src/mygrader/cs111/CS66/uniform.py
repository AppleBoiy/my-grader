import unittest


def uniform(input_str):
    pass


class TestStringFunctions(unittest.TestCase):

    def test_uniform(self):
        # Test uniform function
        test_cases = [
            ("Hello", "hello"),
            ("world", "world"),
            ("HELLO", "HELLO"),
            ("", ""),
            ("123", "123"),
            ("Hello, world!", "hello, world!"),
            ("hElLo, WoRLD!", "HELLO, WORLD!"),
            ("world, WOrld, WORLD!", "world, world, world!"),
        ]
        for input_str, expected_result in test_cases:
            with self.subTest(input_str=input_str):
                self.assertEqual(uniform(input_str), expected_result)


if __name__ == '__main__':
    unittest.main()
