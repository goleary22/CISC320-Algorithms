import unittest
import answer

class TestAnswer(unittest.TestCase):

    def test_sum(self):
        actual = answer.sum_lines(["2\n", "1\n", "3\n"])
        self.assertEqual(actual,"4")

        actual = answer.sum_lines(["5\n", "2\n", "-4\n", "3\n", "1\n", "5\n"])
        self.assertEqual(actual,"11")

        actual = answer.sum_lines(["3\n", "-99\n", "3\n"])
        self.assertEqual(actual,"EMPTY")

        actual = answer.sum_lines([])
        self.assertEqual(actual,"EMPTY")

        actual = answer.sum_lines(["4\n", "6\n", "3\n", "-999\n", "9\n"])
        self.assertEqual(actual,"10")