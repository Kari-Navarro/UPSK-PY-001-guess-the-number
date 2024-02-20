"""Get random number"""
import random

#Correr solo una linea shift + enter
#Limpiar consola con cls
#Sugerencias de escritura crtl + barra espaciadora

user_name = input("Write your name: ")
print("*"*10,"Welcome to the Guess the Number game", user_name,"!","*"*10)
random_number = random.randint(1,100)
lower_limit = 1
higher_limit = 100
player_number = -1
pc = -1
pc_allnumbers = []
player_allnumbers = []
rounds = 0


while player_number != random_number and pc != random_number:
    try:
        rounds = rounds + 1
        print("PC, guess the number between 1 and 100")
        pc = random.randint(lower_limit,higher_limit)
        pc_allnumbers.append(pc)
        print(f"PC: {pc}")
        if pc < random_number:
            print("Too low! Try again")
            lower_limit = pc + 1
        elif pc > random_number:
            print("Too high! Try again")
            higher_limit = pc - 1
        else:
            print("-----The winner is PC-----")
            print("All numbers from PC: ", pc_allnumbers)
            print("All numbers from ", user_name,": ", player_allnumbers)
            
        if pc != random_number:
            player_number = int(input(user_name + ", guess the number between 1 and 100: "))
            player_allnumbers.append(player_number)
            if player_number < random_number:
                print("Too low! Try again")
                if player_number > lower_limit:
                    lower_limit = player_number + 1
            elif player_number > random_number:
                print("Too high! Try again")
                if player_number < higher_limit:
                    higher_limit = player_number - 1
            else:
                print("Congratulations," + user_name + " won!")
                print("All numbers from PC: ", pc_allnumbers)
                print("All numbers from ", user_name,": ", player_allnumbers)

                break
    except ValueError:
        print("Enter only integer numbers")
print("Attempts:",rounds)
