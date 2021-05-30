import unittest

class TestStringMethods(unittest.TestCase):

  def test_lower(self):
      self.assertEqual('HELLO'.lower(), 'hello')

  def test_isupper(self):
      self.assertTrue('HELLO'.isupper())
      self.assertFalse('Hello'.isupper())

if __name__ == '__main__':
    unittest.main()