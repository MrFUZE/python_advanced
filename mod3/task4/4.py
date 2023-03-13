import unittest
from datetime import datetime
from person import Person

class TestPerson(unittest.TestCase):

    def setUp(self):
        self.person = Person('John', 1990)

    def test_get_age(self):
        age = self.person.get_age()
        self.assertEqual(age, datetime.now().year - 1990)

    def test_get_name(self):
        name = self.person.get_name()
        self.assertEqual(name, 'John')

    def test_set_name(self):
        self.person.set_name('Mike')
        name = self.person.get_name()
        self.assertEqual(name, 'Mike')

    def test_set_address(self):
        self.person.set_address('123 Main St')
        address = self.person.get_address()
        self.assertEqual(address, '123 Main St')

    def test_get_address(self):
        address = self.person.get_address()
        self.assertEqual(address, '')

    def test_is_homeless(self):
        is_homeless = self.person.is_homeless()
        self.assertEqual(is_homeless, True)

        self.person.set_address('123 Main St')
        is_homeless = self.person.is_homeless()
        self.assertEqual(is_homeless, False)

if __name__ == '__main__':
    unittest.main()
