import unittest

from week05.zodiac_element.zodiac_element import zodiac_element, yin_yang, animal_year, element_year


class ZodiacElementTests(unittest.TestCase):
    def test_zodiac_element(self):
        # Test cases for zodiac_element function
        self.assertEqual(zodiac_element(2000), "Yang Metal Dragon")
        self.assertEqual(zodiac_element(1988), "Yang Earth Dragon")
        self.assertEqual(zodiac_element(1997), "Yin Fire Ox")
        self.assertEqual(zodiac_element(2022), "Yang Water Tiger")
        self.assertEqual(zodiac_element(1979), "Yin Earth Goat")

    def test_yin_yang(self):
        # Test cases for yin_yang function
        self.assertEqual(yin_yang(2000), "Yang")
        self.assertEqual(yin_yang(1988), "Yang")
        self.assertEqual(yin_yang(1997), "Yin")
        self.assertEqual(yin_yang(2022), "Yang")
        self.assertEqual(yin_yang(1979), "Yin")

    def test_animal_year(self):
        # Test cases for animal_year function
        self.assertEqual(animal_year(2000), "Dragon")
        self.assertEqual(animal_year(1988), "Dragon")
        self.assertEqual(animal_year(1997), "Ox")
        self.assertEqual(animal_year(2022), "Tiger")
        self.assertEqual(animal_year(1979), "Goat")

    def test_element_year(self):
        # Test cases for element_year function
        self.assertEqual(element_year(2000), "Metal")
        self.assertEqual(element_year(1988), "Earth")
        self.assertEqual(element_year(1997), "Fire")
        self.assertEqual(element_year(2022), "Water")
        self.assertEqual(element_year(1979), "Earth")


if __name__ == '__main__':
    unittest.main()
