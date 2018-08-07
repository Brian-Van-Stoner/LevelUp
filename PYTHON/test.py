#for test alwasys import from unit tests
import unittest
from testclass import Phonebook
#inheritances Testcase
class TestPhoneBook(unittest.TestCase):

    def test_creation(self):
        phonebook = Phonebook()
    
    def test_add (self):
        phonebook = Phonebook()
        phonebook.add('bob','0792108346')
        self.assertEqual(len(phonebook.user_details),1)

    def test_search(self):
        phonebook = Phonebook()
        with self.assertRaises(KeyError):
            phonebook.search('tom')
