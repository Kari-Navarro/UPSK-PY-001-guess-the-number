import unittest
from unittest.mock import patch
from functions import  get_random_number, pc_guess, player_guess



class TestGuessNumberFunctions(unittest.TestCase):
    """The name test at the beginning is a convention, and we should call it test in order for the to be executed"""
    def test_get_random_number(self):
        """Test number within a random range"""
        random_number = get_random_number()
        self.assertGreaterEqual(random_number, 1)
        self.assertLessEqual(random_number, 100)
        
    def test_pc_guess(self):
        """Test computer guess with limits"""
        lower_limit = 10
        higher_limit = 90
        pc_number = pc_guess(lower_limit, higher_limit)
        self.assertGreaterEqual(pc_number, lower_limit)
        self.assertLessEqual(pc_number, higher_limit)

    @patch('builtins.input', return_value='10')
    def test_player_guess(self, mock_input):
        "Another test of player_guess function"
        result = player_guess('Karina')
        self.assertEqual(result, 10, 'The function is not working') #the case of failure
        
    #def test_player_guess(self):
    #    """Test player guess with context manager mock and input function"""
    #    user_name = "Karina"
    #    with patch('builtins.input', return_value = '10'):
    #        assert player_guess(user_name) == 10

    #def test_player_guess(self):
        #with unittest.mock.patch('builtins.input', return_value='10'): #context manager
        #    player_number = player_guess("Karina")
        #self.assertIsInstance(player_number, int)

            

if __name__ == '__main__':
#Provides a command-line interface to the test scrip, produces an output that shows the time and number of test
    unittest.main()