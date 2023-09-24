import unittest
from luhn.luhn import luhn_checker


class TestLuhn(unittest.TestCase):
    def test_positive(self):
        self.assertTrue(luhn_checker(5469550017709210))

    def test_negative(self):
        self.assertFalse(luhn_checker(1))
        self.assertFalse(luhn_checker(5469550017079210))
        self.assertFalse(luhn_checker(5469550017009210))

if __name__ == '__main__':
    unittest.main()
