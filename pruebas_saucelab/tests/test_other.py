import unittest

class Test_others(unittest.TestCase):

    def test_equals(self):
        self.assertTrue(1 == 1)

    def test_not_equals(self):
        self.assertFalse(1 == 2)

    def test_contains(self):
        self.assertIn(1,[1,2])