import unittest

from palindrome_without import palindrome_without


class PalindromeWithoutTests(unittest.TestCase):
    def test_palindrome_without_true(self):
        # Test cases that should return True
        self.assertTrue(palindrome_without("level", "e"))
        self.assertTrue(palindrome_without("A man a plan a canal Panama", " "))
        self.assertTrue(palindrome_without("A Santa at NASA", " "))
        self.assertTrue(palindrome_without("Able was I saw Elba", " "))
        self.assertTrue(palindrome_without("racecar", "e"))

    def test_palindrome_without_false(self):
        # Test cases that should return False
        self.assertFalse(palindrome_without("hello", "o"))
        self.assertFalse(palindrome_without("python", "n"))
        self.assertFalse(palindrome_without("algorithm", "r"))
        self.assertFalse(palindrome_without("programming", "g"))

    def test_palindrome_without_empty_string(self):
        # Test case with empty string
        self.assertFalse(palindrome_without("", "a"))

    def test_palindrome_without_single_character(self):
        # Test case with single character
        self.assertTrue(palindrome_without("b", "a"))
        self.assertFalse(palindrome_without("a", "a"))

    def test_palindrome_without_case_sensitive(self):
        # Test case with case sensitivity
        self.assertTrue(palindrome_without("Racecar", "e"))
        self.assertTrue(palindrome_without("Level", "e"))


if __name__ == '__main__':
    unittest.main()
