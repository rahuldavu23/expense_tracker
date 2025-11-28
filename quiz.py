print("Welcome to the computer quiz!")
#this would be a variable where I am assigning a value to it
playing = input("Do you want to play?").lower()
#^ is also taking in an input via the input() from the user, we have the .lower just to make sure the users inputted gets lowercased

if playing != "yes": 
    quit()

print("Ok lets do this!")
score = 0
answer = input("Who was the first canonical Super Saiyan in DBZ?").lower()
if answer == ("goku").lower():
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("Who was the one to actually kill Frieza in DBZ?").lower()
if answer == ("trunks").lower():
    print("Correct!")
    score += 1
else: 
    print("Incorrect!")

answer = input("What is the name of Goku's father?").lower()
if answer == ("bardock").lower():
    print("Correct!")
    score += 1
else: 
    print("Incorect!")

if score >= 2:
    print("Wow not bad!")
else:
    print("You're ass")
