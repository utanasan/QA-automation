import unittest
import multiply_even


class MultiplyEven(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(
            multiply_even.multiply([2,3,4,5,6]),
            48)


if __name__ == '__main__':
    unittest.main()
