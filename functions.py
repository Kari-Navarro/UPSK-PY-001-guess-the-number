"""Get random number"""

import random

def get_random_number():
    return random.randint(1,100)

def pc_guess(lower_limit, higher_limit):
    return random.randint(lower_limit, higher_limit)

def player_guess(user_name):
    return int(input(user_name + ", guess the number between 1 and 100: "))

#def pc_guess(random_number, boolean_pc, lower_limit, higher_limit):
    
#    pc_number = random.randint(1,100)
#    print(f"PC:{pc_number}" )


#    if pc_number < random_number:
#        print("Too low! Try again")
#        lower_limit = pc_number + 1
#    elif pc_number > random_number:
#        print("Too high! Try again")
#        higher_limit = pc_number - 1
#    else:
#        print("-----The winner is PC-----")
#        boolean_pc = True
#    return boolean_pc, lower_limit, higher_limit, pc_number





#def player_guess(random_number, boolean_user, lower_limit, higher_limit, user_name):
    
#    player_number = int(input(f"{user_name}, guess a number between 1 and 100 ")) 
#    print(f"{user_name}: {player_number}")

#    if player_number < random_number:
#        print("Too low! Try again")
#        lower_limit = player_number + 1  
#    elif player_number > random_number:
#        print("Too high!, Try again")
#        higher_limit = player_number - 1  
#    else:
#        print(f"-----Congratulations,{user_name} won!-----")
#        boolean_user = True
#    return boolean_user, lower_limit, higher_limit, player_number
