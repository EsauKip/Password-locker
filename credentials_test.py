#!usr/bin/env python3.9
import unittest#import unittest module
from credentials import Credentials
class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_credentials = Credentials("Gmail", "kipronoesau28@gmail.com", "kiprono2022")
#6th test
    def test_init(self):
        '''
        check if instances initialize as expected
        '''
        self.assertEqual(self.new_credentials.account, "Gmail")
        self.assertEqual(self.new_credentials.email, "kipronoesau28@gmail.com")
        self.assertEqual(self.new_credentials.password, "kiprono2022")
        #7th test
    def test_save_credentials(self):
        '''
        check if credentials can be saved
        '''  
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)
#save multiple credentials
    def test_saving_multiple_credentials(self):
        '''
        check if users can store multiple credentials
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "trythis","passcode")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)
    def tearDown(self):
        '''
        clear list before any test is run
        '''
        Credentials.credentials_list = []
#delete credentials 
    def test_delete_credentials(self):
        '''
        test if you can delete credentials test
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter", "trythis","passcode")
        test_credentials.save_credentials()
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list), 1)



if __name__ == "__main__":
    unittest.main()