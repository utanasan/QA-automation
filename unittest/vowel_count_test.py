import unittest
import vowel_count


class VowelEven(unittest.TestCase):
    def test_vowelcount(self):
        self.assertEqual(
           vowel_count.vowel("Helicopter and airplane"),
            {'e': 3, 'i': 2, 'o': 1, 'a': 3}
        )


if __name__ == '__main__':
    unittest.main()
