import unittest
import answer

class TestAnswer(unittest.TestCase):

    def test_sum(self):
        actual = answer.summation(["2\n", "1\n", "3\n"])
        self.assertEqual(actual,6)

        #testing negatives
        actual = answer.summation(["5\n", "2\n", "-4\n", "3\n", "1\n", "5\n"])
        self.assertEqual(actual,16)
        
        #testing -999 break
        actual = answer.summation(["3\n", "-999\n", "3\n"])
        self.assertEqual(actual,3)

        #testing empty
        actual = answer.summation([])
        self.assertEqual(actual,"EMPTY")

        #testing -999 break
        actual = answer.summation(["-999\n", "3\n"])
        self.assertEqual(actual,"EMPTY")

        #testing -999 break
        actual = answer.summation (["4\n", "6\n", "3\n", "-999\n", "9\n"])
        self.assertEqual(actual,13)