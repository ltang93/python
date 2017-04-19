import unittest


class MyTestCase(unittest.TestCase):
    def setUp(self):
        print('setUp')
    def test_something(self):
        print('1')
        self.assertEqual(False, False)
    def test_something1(self):
        print('2')
        self.assertEqual(True, True)
    def tearDown(self):
        print('tearDown')

if __name__ == '__main__':
    unittest.main()
