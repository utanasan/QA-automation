import unittest
import full_name


class MyTestCase(unittest.TestCase):
    def test_normal(self):
        self.assertEqual(
            full_name.full_name('Завгороднева',
                                'Елена',
                                'Сергеевна'),
            'Завгороднева Елена Сергеевна'
        )

    def test_big(self):
        self.assertEqual(
            full_name.full_name('ЗАВГОРОДНЕВА',
                                'ЕЛЕНА',
                                'СЕРГЕЕВНА'),
            'Завгороднева Елена Сергеевна'
        )

    def test_small(self):
        self.assertEqual(
            full_name.full_name('завгороднева',
                                'елена',
                                'сергеевна'),
            'Завгороднева Елена Сергеевна'
        )

if __name__ == '__main__':
    unittest.main()
