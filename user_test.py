#!usr/bin/env python3.9
import unittest #import unittestmodule
from user import User #import the user class
class User(unittest.TestCase):
    def setUp(self):
        '''
        method to run before each test
        '''
        self.new_user=User("EsauKip","#Youcannotfind5") #new User created

    def tearDown(self):
        '''
        clean up after each test to prevent errors
        '''
        User.user_list = []
    def test__init(self):
       
        self.assertEqual(self.new_user.username, "EsauKip")
        self.assertEqual(self.new_user.password, "#Youcannotfind5")
        ##second test

 
if __name__ == "__main__":
    unittest.main()