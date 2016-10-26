import random
import time
def guessMyNumber():
    
    print("Hello Change")
    
    print("Hello Pete, welcome to Guess My Number")
    time.sleep(1)
    print ("The computer is thinking of a number between 1-100")
    time.sleep(2)
    print("Try to guess the number in as few attempts as possible")
    number=random.randint(1,100)
    tries = 1
    errorCheck = "true"
    while errorCheck == "true":
        try:
            guess =int(input("Take a guess "))
            while guess !=number:
                try:
                    if guess>number:
                        print("You need to go lower")
                        guess =int(input("Take another guess "))
                    else:
                       print("Go higher!")
                       guess =int(input("Take another guess "))
                except ValueError:
                    print("You must enter a whole number")
                    guess=int(input("Please take another guess, making sure that it is a whole number. Thank you. "))
                    tries=tries+1               
            if tries < 5:
                print("Well done Pete! You guessed the number in", tries, "tries! If you would like to play again please type 'guessMyNumber()'")
            else:
                print("You guessed the number in", tries, "tries. If you would like to play again type 'guessMyNumber()' ")
        except ValueError:
            print("You must enter a whole number")
            print("Please make sure that you have written an integer e.g '1, 2, 3', thank you")
            time.sleep(2)
            print("Please take another guess, making sure that it is a whole number. Thank you. ")
            tries=tries+1
        else:
            errorCheck == "false"
            
guessMyNumber()
