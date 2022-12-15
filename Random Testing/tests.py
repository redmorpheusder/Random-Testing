import unittest
from credit_card_validator import credit_card_validator
import random


class TestCase(unittest.TestCase):
    def testrand(self):
        for i in range(0, 1000000):
            val = random.randint(10000000000000, 9999999999999999)
            credit_card_validator(val)


if __name__ == '__main__':
    unittest.main()
