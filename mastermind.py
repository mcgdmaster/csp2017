# number guesser game :D
ba=[0]    #set global variable
import random    #telling the computer i'm going to get a random number
i = 0    #setting a local variable
while i < 1:    #creating a counting loop
    n = random.randint(1, 20)    # to choose a number
    i +=1    #add one
print ('Hello, and welcome to Number Guesser!')    #say that
print ('What is your name?')    #also say that
name = raw_input()    #waiting on input
print ('How confident are you, ' + name + '?')    #taking your name
print ('I have chosen a number between 1-20. Can you guess it in 3 guesses?')    #say that
def guess ():    #the guess section
    global ba    #calling on global variable
    while(ba[0] <3):    #creating loop
        p = raw_input()    #waiting for input
        p = (int(p))    #changing it to an integer
        if (p < 1 or p > 20):    #testing to see if guess is outside variables
            print ('Um, that is a number outside of the numbers I alotted you...')    #say that
        elif (n == p):    #a second option
            print ('You guessed it!')    #say that
            riddle()    #go to riddle definition
        else:    #else
            print ('you have used')    #say that
            print (ba[0]+1)    #say the guesses taken
            print ('guesses')   # say that
            add()    #go to add definition
    print 'Game over!'    #say that
def add():    #add definition
    ba[0]=(ba[0]+1)    #add one to variable
    guess ()    #go back to guess definition
def riddle ():    #the riddle definition
    print ('Would you like a riddle? 1/2?')    #say that, i used a number instead of words because words seem to cause a problem
    print ('1 is yes and 2 is no, by the way')    #say that
    c = raw_input()    #waiting for input
    c = (int(c))    #change it to an integer
    if (c == 1):    #test this statement
        print ('OK, you asked for it, ' + name + '...')    #say that and name
        print ('You are in a room with a solid floor, roof, and walls')    #say the first part of the riddle
        print ('There is only a mirror')    #say the second part of the riddle
        print ('How do you get out?')    #the last part of the riddle
    elif (c == 2):    #test this
        print ('Oh, OK. :(')    #say that
    else: #else
        print('Thats not what I asked for')    #say that
        riddle()    #go back to riddle definition
guess ()    #this starts the program