import random

number = random.randint(0, 100)
# print(number)

while True:
    user_input = int(input("Guess the number... \n"))
    
    if user_input > number:
        print("Too high, guess again.")
    elif user_input < number:
        print("Too low, guess again.")
    else:
        print("Just right!")
        break