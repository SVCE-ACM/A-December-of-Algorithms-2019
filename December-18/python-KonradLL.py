# Input: T!Kk@
# Output: Time taken: 691.266026974 seconds

import sys
import threading
import numpy
import time

passwordToCrack = None
cracked = False
allowedCharacters = [' ',  '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~']

threadSize = 10
startTime = time.time()


def main():
    global passwordToCrack
    passwordToCrack = sys.argv[1]
    if not passwordToCrack:
        print('password is not given')
    
    global startTime
    startTime = time.time()
        
    for arr in numpy.array_split(allowedCharacters, threadSize):
        thread = threading.Thread(target=startThread, args=(arr, len(passwordToCrack), ) )
        thread.start()



def startThread(startingCharacters, length):
    for char in startingCharacters:
        if length == 1:
            if char == passwordToCrack:
                cracked = True
                print "cracked the password"
        else:
            bruteForce(char, length - 1)


def bruteForce(password, remainingLength):
    global cracked
    global passwordToCrack
    for char in allowedCharacters:
        if cracked is True:
            break

        currPassword = password + char
        if remainingLength <= 1:
            if currPassword == passwordToCrack:
                cracked = True
                stopTimer()
        else:
            bruteForce(currPassword, remainingLength - 1)
            

def stopTimer():
    stopTime = time.time()
    print "Time taken: " + str(stopTime - startTime) + " seconds"




if __name__ == "__main__":
    main()