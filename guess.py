import random as rd

number = rd.randint(1,11)
isguestr = False

while isguestr != True:
    guess= input("Please guess the number")
    if int(guess) == number:
        print("Very good you guess a number {} secret number {}".format(guess,number))
    else:
        print("{} isn't secret number".format(guess))
