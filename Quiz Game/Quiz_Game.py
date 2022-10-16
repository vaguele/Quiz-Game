print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
score = 0
if playing.lower() != "yes":
    quit() #will terminate the program
print("Okay! Let's Play:) ")
answer = input("What does CPU stand for? ").lower() #.lower() works in both line 6 and 7's instances
if answer.lower() == "central processing unit":     
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
answer = input("What does PSU stand for? ")
if answer.lower() == "power supply unit":
    print("Correct!")
    score +=1
else:
    print("Incorrect!")
    
    print("You got " + str(score) + " questions correct;") #string(score) converts the "int" varible score into a "string"
    print("You got " + str((score/4) * 100) + "%")

