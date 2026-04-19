print("Welcome To My Quiz Game!")

playing = input("Do you want to play this game(yes/no)? ")

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")
score=0

answer=input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("Correct! You have 1 point :)")
    score+=1
else:
    print("Incorrect :(")

answer=input("What does GPU stands for? ")
if answer.lower() == "graphics processing unit":
    print("Correct! You have 1 point :)")
    score+=1
else:
    print("Incorrect :(")


answer=input("What does RAM stands for? ")
if answer.lower() == "random access memory":
    print("Correct! You have 1 point :)")
    score+=1
else:
    print("Incorrect :(")

answer=input("What does ROM stands for? ")
if answer.lower() == "read only memory":
    print("Correct! You have 1 point :)")
    score+=1
else:
    print("Incorrect :(")

answer=input("What does PSU stands for? ")
if answer.lower() == "power supply":
    print("Correct! You have 1 point :)")
    score+=1
else:
    print("Incorrect :(")

print("You got "+str(score)+ " answers correct!")
print("You got "+str((score/5)*100) +"%.")
print("Thank you for playing my quiz game :)")