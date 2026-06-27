import unittest
from Dec2Hex import decimal_to_hex

class TestDecimalToHex(unittest.TestCase):

    def test_valid_input(self):
        # Test that 25 converts correctly to 19 in hex
        self.assertEqual(decimal_to_hex(25), '19')

    def test_valid_input_15(self):
        # Test that 15 converts correctly to F in hex
        self.assertEqual(decimal_to_hex(15), 'F')

    def test_valid_input_255(self):
        # Test that 255 converts correctly to FF in hex
        self.assertEqual(decimal_to_hex(255), 'FF')

if __name__ == '__main__':
    unittest.main()
