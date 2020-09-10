import unittest

from src.high_scores import *

# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    # Test latest score (the last thing in the list)
    def test_latest(self):
        my_scores = [10, 20, 50, 40, 30, 50, 30]
        self.assertEqual(30, latest(my_scores))

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        my_scores = [10, 20, 50, 50, 40, 30, 50, 30]
        self.assertEqual(50, personal_best(my_scores))

    # Test top three from list of scores
    def test_personal_top_three(self):
        my_scores = [10, 20, 50, 50, 40, 30, 50, 30]
        self.assertEqual([50, 50, 50], personal_top_three(my_scores))

    # Test ordered from highest tp lowest
    def test_high_to_low(self):
        my_scores = [10, 20, 50, 50, 40, 30, 50, 30]
        self.assertEqual([50, 50, 50, 40, 30, 30, 20, 10], high_to_low(my_scores))

    # Test top three when there is a tie
    def test_top_three_when_there_is_a_tie(self):
        my_scores = [10, 20, 50, 50, 40, 30, 50, 30]
        self.assertEqual([50, 50, 50], personal_top_three(my_scores))

    # Test top three when there are less than three
    def test_top_three_when_there_are_less_than_three(self):
        my_scores = [50, 30]
        self.assertEqual([50, 30], personal_top_three(my_scores))

    # Test top three when there is only one
    def test_top_three_when_there_is_only_one(self):
        my_scores = [50]
        self.assertEqual([50], personal_top_three(my_scores))
    
