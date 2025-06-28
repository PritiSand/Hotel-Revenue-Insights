print("Welcome to the game! ")

playing = input("Do you want to play the quiz? ")

if playing.lower() == "yes":
    print("Okay! Let's play :) ")
else:
    quit()
score = 0

answer1 = input("Which planet is known as the Red Planet? ")
if answer1.lower() == "mars":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer2 = input("In which year did India win its first Cricket World Cup? ")
if answer2.lower() == "1983":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer3 = input("Who is the founder of Microsoft? ")
if answer3.lower() == "bill gates":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer4 = input("What is the largest mammal in the world? ")
if answer4.lower() == "blue whale":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer5 = input("What is the powerhouse of the cell? ")
if answer5.lower() == "mitochondria":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

percentage=(score/5)*100
print("Congratulations! You have completed the quiz.")
print("Score: " + str(score) + "/5")
print("Percentage: " , percentage)

if percentage == 100:
    print("🏆 Excellent! You're a quiz master! 🎯")
elif percentage >= 60:
    print("👍 Well done! You did great! 👏")
else:
    print("😅 Keep practicing! You'll do better next time. 💪")