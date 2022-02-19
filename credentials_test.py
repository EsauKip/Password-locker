import unittest#import unittest module
from credentials import Credentials
class TestCredentials(unittest.TestCase):
    def setUp(self):
        self.new_cred = Credentials("Gmail", "kipronoesau28@gmail.com", "kiprono2022")
