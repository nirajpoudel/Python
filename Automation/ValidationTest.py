import unittest

from ValidateUser import validate_user

class TestValidateUser(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(validate_user('validuser',3),True)

    def test_too_short(self):
        self.assertEqual(validate_user('inv',5),False)

    def test_invalid_character(self):
        self.assertEqual(validate_user('Invalid_user',1),False)

    def test_invalid_minlen(self):
        self.assertRaises(ValueError,validate_user,'user',-1)

unittest.main()
        
