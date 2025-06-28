import random

top_of_range = input("Enter a number to set the guessing range: ")
if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range<=0:
        print("Please enter a number greater then 0!")

else:
    print("Please enter a number next time!")

random_number = random.randint(1, top_of_range)
guesses = 0

while True:
    guesses +=1
    user_input = input("Enter your guess: ")

    if user_input.isdigit():
        user_input = int(user_input)

    else:
        print("Please type a number next time!")
        continue 

    if user_input == random_number:
        print("You got it correct!")
        break
    elif user_input < random_number:
        print("You are below the number!")
    else: 
        print("You are above the number!")

print("Yayy!! You have guessed the correct number in" , guesses ,  "guesses.")