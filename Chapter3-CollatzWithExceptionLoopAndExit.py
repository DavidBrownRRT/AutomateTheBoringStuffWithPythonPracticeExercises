#Author: David A Brown
#Collatz loop with exception handling for non-integer entry
#Escape command using zero
#Error message generated for use of negative number

import sys
def collatz(number):
    while True:
        try:
            number = int(input("Enter an integer > 1 for Collatz analysis. Enter '0' to exit:\n")) 
            
            while True:
                if number == 0:
                    sys.exit(print('Exiting program'))
                elif number < 0:
                    print('ERROR: Number must be an integer and > 1.')
                    break
                elif number == 1:
                    break
                elif number % 2 == 0:
                    number = number // 2
                else:
                    number = 3 * number + 1
                print(number)
                
        except ValueError:
            print('ERROR: Number must be an integer and > 1.')

number = None
collatz(number)
