import unittest
import re
from string import punctuation
from password_requirements import password_requirements as pr
from strong_password_generator import strong_password_generator

password = strong_password_generator()


class TestStrongPasswordGenerator(unittest.TestCase):

    def test_strong_password_generator(self):
        self.assertIsNotNone(re.search("[a-z]", password), pr["upper_lower_chars"])
        self.assertIsNotNone(re.search("[A-Z]", password), pr["upper_lower_chars"])
        self.assertIsNotNone(re.search("[0-9]", password), pr["digits"])
        self.assertIsNotNone(re.search("[" + punctuation + "]", password), pr["punctuation"])
        self.assertTrue(14 <= len(password) <= 64, pr["length"])
