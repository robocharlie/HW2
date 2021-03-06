# Continually generate random integers between 1 and 10 (ook at the random.randint() function in the python standard
# library for help) to simulate the roll of a 10-sided die Print each random value to the terminal with a .1s delay
# between numbers. Stop only when a generated number is 8, 9, or 10, and print to terminal "Roll X resulted in a value
# of Y" where X is the # of rolls and Y is the value of the die.


from random import randint
from time import sleep

high_roll = False
roll_number = 0
while not high_roll:
    num = randint(1, 10)
    roll_number += 1
    if num >= 8:
        print('Roll {} resulted in a value of {}'.format(roll_number, num))
        high_roll = True
    else:
        print(num)
    sleep(.1)
