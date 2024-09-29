import unittest

from lp_solvers.simplex import simplex

class TestStringMethods(unittest.TestCase):

    def test_simplex(self):
        self.assertEqual('foo'.upper(), 'FOO')

if __name__ == '__main__':
    unittest.main()