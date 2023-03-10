import unittest
from testprograms import program1
class My_test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(program1.add_two_numbers(10,20),30)
    def test_case2(self):
        self.assertEqual(program1.add_two_numbers(-10,-30),-40)
    def test_case2(self):
        self.assertEqual(program1.add_two_numbers(-10,10),0)
    def test_case2(self):
        self.assertEqual(program1.add_two_numbers(-40,3),-37)
    def test_case2(self):
        self.assertEqual(program1.add_two_numbers(10.5,30.6),41.1)
    def test_case2(self):
        self.assertEqual(program1.add_two_numbers(-10.5,-30.6),-41.1)
    def test_case2(self):
        self.assertEqual(program1.add_two_numbers(-10.5,30.5),20.0)
    def test_case2(self):
        self.assertEqual(program1.add_two_numbers(10.5,-30.5),-20.0)
