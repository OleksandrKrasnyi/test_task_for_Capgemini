import unittest
import string
from password_requirements import password_requirements as pr
from password_checker import password_checker


class TestPasswordChecker(unittest.TestCase):
    def test_password_checker(self):
        self.assertEqual(password_checker("Hx4NC:#WagdLEUgwftND"),
                         [])

        self.assertEqual(password_checker(""),
                         [pr["upper_lower_chars"],
                          pr["digits"],
                          pr["punctuation"],
                          pr["length"]])

        self.assertEqual(password_checker("A"),
                         [pr["upper_lower_chars"],
                          pr["digits"],
                          pr["punctuation"],
                          pr["length"]])

        self.assertEqual(password_checker("a"),
                         [pr["upper_lower_chars"],
                          pr["digits"],
                          pr["punctuation"],
                          pr["length"]])

        self.assertEqual(password_checker("Aa"),
                         [pr["digits"],
                          pr["punctuation"],
                          pr["length"]])

        self.assertEqual(password_checker("0"),
                         [pr["upper_lower_chars"],
                          pr["punctuation"],
                          pr["length"]])

        self.assertEqual(password_checker("@#$%"),
                         [pr["upper_lower_chars"],
                          pr["digits"],
                          pr["length"]])

        self.assertEqual(password_checker("MORE_THAN_64_CHARACTERS"
                                          + string.ascii_letters
                                          + string.digits
                                          + string.punctuation),
                         [pr["length"]])

        self.assertEqual(password_checker("Qq&0"),
                         [pr["length"]])

        self.assertIsNone(password_checker("ПАРОЛЬ_НЕ_ASCII"))
