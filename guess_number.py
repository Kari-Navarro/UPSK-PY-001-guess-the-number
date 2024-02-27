from functions import get_random_number
from functions import pc_guess
from functions import player_guess


def guess_number():
    while True:
        user_name = input("Write your name: ")
        print("*"*10,"Welcome to the Guess the Number game", user_name,"!","*"*10)
        lower_limit = 1
        higher_limit = 100
        pc_all_numbers = []
        player_all_numbers = []
        rounds = 0
        random_number = get_random_number()
        user = -1
        computer = -1

        while user != random_number and computer != random_number:
            try: 
                rounds += 1
                pc = pc_guess(lower_limit, higher_limit)
                pc_all_numbers.append(pc)
                print(f"PC: {pc}")
                if pc == random_number:
                    print("-----The winner is PC-----")
                    break
                elif pc < random_number:
                    print("Too low! Try again")
                    lower_limit  = pc + 1
                else:
                    print("Too high! Try again")
                    higher_limit = pc - 1

                player_number = player_guess(user_name)
                player_all_numbers.append(player_number)
                if player_number == random_number:
                    print("Congratulations,"+user_name+"won!")
                    break
                elif player_number < random_number:
                    print("Too low! Try again")
                    if player_number > lower_limit:
                        lower_limit = player_number + 1
                else:
                    print("Too high! Try again")
                    if player_number < higher_limit:
                        higher_limit = player_number - 1

            except ValueError:
                print("Enter only integers numbers")
        print("All numbers from PC: ", pc_all_numbers)
        print("All numbers from ", user_name,": ", player_all_numbers)
        print("Attempts:", rounds)


        play = input("Do yo want to play again)(yes/no): ")
        if play.lower() != "yes":
            print("Goodbye!")
            break 

guess_number()