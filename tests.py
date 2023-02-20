import unittest
import answer

class TestAnswer(unittest.TestCase):

    def test_sum(self):
        actual = answer.summation(["2\n", "1\n", "3\n"])
        self.assertEqual(actual,6)

        actual = answer.summation(["5\n", "2\n", "-4\n", "3\n", "1\n", "5\n"])
        self.assertEqual(actual,16)

        actual = answer.summation(["3\n", "-999\n", "3\n"])
        self.assertEqual(actual,3)

        actual = answer.summation([])
        self.assertEqual(actual,"EMPTY")

        actual = answer.summation(["-999\n", "3\n"])
        self.assertEqual(actual,"EMPTY")

        actual = answer.summation (["4\n", "6\n", "3\n", "-999\n", "9\n"])
        self.assertEqual(actual,13)