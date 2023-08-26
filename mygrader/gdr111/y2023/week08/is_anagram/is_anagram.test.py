import unittest
import sort_is_anagram

from faker import Faker
from mygrader import print_test_results
from map_is_anagram import is_anagram


class TestIsAnagram(unittest.TestCase):

    def setUp(self):
        self.fake = Faker()

    def test_anagrams(self):
        self.assertTrue(is_anagram("listen", "silent"))
        self.assertTrue(is_anagram("The Morse Code", "Here come dots"))
        self.assertTrue(is_anagram("debit card", "bad credit"))

    def test_non_anagrams(self):
        self.assertFalse(is_anagram("hello", "world"))
        self.assertFalse(is_anagram("python", "java"))
        self.assertFalse(is_anagram("test", "text"))

    def test_mixed_case_anagrams(self):
        self.assertTrue(is_anagram("Anagram", "Nagaram"))
        self.assertTrue(is_anagram("Astronomer", "Moon starer"))
        self.assertTrue(is_anagram("The eyes", "They see"))

    def test_empty_strings(self):
        self.assertTrue(is_anagram("", ""))
        self.assertFalse(is_anagram("hello", ""))
        self.assertFalse(is_anagram("", "world"))

    def test_random_anagrams(self):
        num_test_cases = 1_000_000
        num_passed = 0
        num_failed = 0
        failed_cases = []

        print()

        for i in range(1_000_000):  # Generate and test 1000 random anagrams
            word = self.fake.sentence(nb_words=1, variable_nb_words=True, ext_word_list=None)
            # Generate a random anagram by shuffling the characters of the word
            anagram = ''.join(self.fake.random_choices(word, length=len(word)))

            expected = is_anagram(word, anagram)
            result = sort_is_anagram.is_anagram(word, anagram)

            if expected != result:
                num_failed += 1
                if num_failed <= 1000:
                    failed_cases.append(((word, anagram), expected, result))

            else:
                num_passed += 1

            # Print prompt every 100,000 cases
            if i % 100000 == 0:
                print(f"{i} out of {num_test_cases} test cases tested.")


        print_test_results(num_passed, num_failed, failed_cases, True)




if __name__ == "__main__":
    unittest.main()
