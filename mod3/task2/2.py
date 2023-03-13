import unittest
from decrypt import decrypt

class DecryptTestCase(unittest.TestCase):

    def test_no_dots(self):
        cipher = "abra-cadabra."
        expected = "abra-cadabra"
        result = decrypt(cipher)
        self.assertEqual(result, expected)

    def test_one_dot(self):
        cipher = "abraa...-cadabra"
        expected = "abra-cadabra"
        result = decrypt(cipher)
        self.assertEqual(result, expected)

    def test_two_dots(self):
        cipher = "abra--..-cadabra"
        expected = "abra-cadabra"
        result = decrypt(cipher)
        self.assertEqual(result, expected)

    def test_three_dots(self):
        cipher = "abrau...-cadabra"
        expected = "abra-cadabra"
        result = decrypt(cipher)
        self.assertEqual(result, expected)

    def test_many_dots(self):
        cipher = "abr........"
        expected = ""
        result = decrypt(cipher)
        self.assertEqual(result, expected)

    def test_dots_and_chars(self):
        cipher = "abr......a."
        expected = "a"
        result = decrypt(cipher)
        self.assertEqual(result, expected)

    def test_digits_and_dots(self):
        cipher = "1..2.3"
        expected = "23"
        result = decrypt(cipher)
        self.assertEqual(result, expected)

    def test_only_dot(self):
        cipher = "."
        expected = ""
        result = decrypt(cipher)
        self.assertEqual(result, expected)

    def test_many_dots_no_chars(self):
        cipher = "1......................."
        expected = ""
        result = decrypt(cipher)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
