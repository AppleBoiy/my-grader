import unittest


def substitute_once(text, old, new):
    pass


class TextSubstitutionTest(unittest.TestCase):
    def test_substitute_once(self):
        # Test case 1: Substitute "fox" with "dog"
        text = "The quick brown fox jumps over the lazy dog."
        old = "fox"
        new = "dog"
        expected_result = "The quick brown dog jumps over the lazy dog."

        result = substitute_once(text, old, new)

        self.assertEqual(result, expected_result)

    def test_substitute_once_no_match(self):
        # Test case 2: No match found, text remains unchanged
        text = "Hello, world!"
        old = "planet"
        new = "universe"
        expected_result = "Hello, world!"

        result = substitute_once(text, old, new)

        self.assertEqual(result, expected_result)

    def test_substitute_once_multiple_matches(self):
        # Test case 3: Only the first occurrence is replaced
        text = "Hello, hello, hello!"
        old = "hello"
        new = "hi"
        expected_result = "Hello, hi, hello!"

        result = substitute_once(text, old, new)

        self.assertEqual(result, expected_result)

    def test_substitute_once_empty_text(self):
        # Test case 4: Empty text, should return an empty string
        text = ""
        old = "apple"
        new = "orange"
        expected_result = ""

        result = substitute_once(text, old, new)

        self.assertEqual(result, expected_result)

    def test_substitute_once_empty_old(self):
        # Test case 5: Empty old string, should return the original text
        text = "The cat sat on the mat."
        old = ""
        new = "dog"
        expected_result = "The cat sat on the mat."

        result = substitute_once(text, old, new)

        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
