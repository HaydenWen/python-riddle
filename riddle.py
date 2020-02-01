#!/usr/bin/python3

# A small program designed to demonstrate some basic concepts in Python. 
#
# Written by Hayden Wen

def main():

    attempts = 0

    """ Loop infinitely until the correct answer is given"""
    while(True):

        guess = input("Give me a number that generates itself.\n")

        """ Checking for valid input """
        if(checkValidInput(guess)):
    
            result = generateNumber(guess)
            """ Checking if the result generates itself """
            if(result == guess):
                
                print(result)
                print("Congratulations!", guess, "does indeed \
                generate itself! Goodbye.")
                break
            elif(attempts < 100):

                print(result)
            else: 
                print("Stop trying to brute force the solution :)")
            attempts += 1
            
def checkValidInput(guess):

    """ Function which takes a string and determines if it is a positive 
    integer that contains more than 4 digits.

    :param guess: String 
    :return: Boolean
    """
    
    if(guess.isdigit() == False):
        print("Not a valid number")
        return False
    elif(len(guess) < 4):
        print("Not large enough")
        return False

    return True

def generateNumber(guess):
    """ Function which takes a valid guess in the form of a string and 
    generates the string of its corresponding number

    :param guess: String
    :return: String
    """
    result = ""
    digitFrequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for digit in guess:

        digitFrequency[int(digit)] += 1
    i = 0
    while(i < len(digitFrequency)):

        if(digitFrequency[i]):
            result = result + str(digitFrequency[i]) + str(i)
        i += 1
    return result


if __name__ == "__main__":
    main()
