import unittest
from string import ascii_lowercase as ct

from decodeV1 import decode_line, decode_helper, decode


class TestDecodeFunctions(unittest.TestCase):

    def test_decode(self):
        txt = "1 2 3 .\n4 5 6 .\n7 8 9 ."
        expected_result = "bcd\nefg\nhij"
        decoded_text = decode(ct, txt)
        self.assertEqual(decoded_text, expected_result)

    def test_decode_line(self):
        line1 = "1 2 3 ."
        line2 = "4 5 6 ."
        result1 = "bcd"
        result2 = "efg"
        decoded1 = decode_line(ct)(line1)
        decoded2 = decode_line(ct)(line2)
        self.assertEqual(decoded1, result1)
        self.assertEqual(decoded2, result2)

    def test_decode_helper(self):
        idx1 = "1"
        idx2 = "25"
        idx3 = "100"
        result1 = "b"
        result2 = "z"
        result3 = "_"
        decoded1 = decode_helper(ct)(idx1)
        decoded2 = decode_helper(ct)(idx2)
        decoded3 = decode_helper(ct)(idx3)
        self.assertEqual(decoded1, result1)
        self.assertEqual(decoded2, result2)
        self.assertEqual(decoded3, result3)


if __name__ == '__main__':
    unittest.main()
