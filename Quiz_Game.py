print("welcome to my computer quiz!")
#prints the string
playing = input("do you want to play? ")
#defines the variable and asks the user for input
if playing.lower() != "yes":
#if the user input is not "yes" then the program will end
    quit()
    #quit funcaton in python will end the program
print("okay! let's play :)")
score = 0
#prints a string
answer = input("what does cpu stand for? ")
#defines the variable and asks the user for input
if answer.lower() == "central processing unit":
#if is followed by a condition, if the condition is true then the code block will be executed
    print("correct!")
    score += 1
else:   
    print("incorrect!")
#if the condition is false then the code block after else will be executed
answer = input("What does gpu stand for? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:   
    print("incorrect!")
answer = input("What does ram stand for? ")
if answer.lower() == "random access memory":
    print("correct!")
    score += 1  
else:   
    print("incorrect!")
answer = input("What does rom stand for? ")
if answer.lower() == "read-only memory":
    print("correct!")
    score += 1
else:   
    print("incorrect!")    
answer = input("What does psu stand for? ")
if answer.lower() == "power supply unit":
    print("correct!")
    score += 1
else:   
    print("incorrect!")    
print("you got " + str(score) + " questions correct!")
# + is used to concatenate strings, str() function is used to convert the score variable to a string so it can be concatenated with the other strings.
print("you got " + str((score / 5) * 100) + "%.")
