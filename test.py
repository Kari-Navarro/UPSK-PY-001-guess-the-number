import unittest
from unittest.mock import patch
from functions import  get_random_number, pc_guess, player_guess



class TestGuessNumberFunctions(unittest.TestCase):
    def test_get_random_number(self):
        #Test number within a random range
        random_number = get_random_number()
        self.assertGreaterEqual(random_number, 1)
        self.assertLessEqual(random_number, 100)
    
    def test_pc_guess(self):
        guess = pc_guess(1,100)
        self.assertGreaterEqual(guess, 1)
        self.assertLessEqual(guess, 100)

    @patch("builtins.input", return_value="10")
    def test_player_guess(self, mock_input):
        user_name = "Karina"
        self.assertEqual(player_guess(user_name), 50)
        


if __name__ == '__main__':
#Provides a command-line interface to the test scrip, produces an output that shows the time and number of test
    unittest.main()