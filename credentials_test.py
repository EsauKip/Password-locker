#!usr/bin/env python3.9
import unittest#import unittest module
from credentials import Credentials
class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_cred = Credentials("Gmail", "kipronoesau28@gmail.com", "kiprono2022")
#6th test
    def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_cred.account, "Gmail")
        self.assertEqual(self.new_cred.email, "kipronoesau28@gmail.com")
        self.assertEqual(self.new_cred.password, "kiprono2022")
if __name__ == "__main__":
    unittest.main()