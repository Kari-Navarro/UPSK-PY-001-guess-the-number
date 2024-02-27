"""Get random number"""

import random

def get_random_number():
    return random.randint(1,100)

def pc_guess(lower_limit, higher_limit):
    return random.randint(lower_limit, higher_limit)

def player_guess(user_name):
    return int(input(user_name + ", guess the number between 1 and 100: "))
