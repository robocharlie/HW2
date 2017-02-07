# Continually generate random integers between 1 and 10 (ook at the random.randint() function in the python standard
# library for help) to simulate the roll of a 10-sided die Print each random value to the terminal with a .1s delay
# between numbers. Stop only when a generated number is 8, 9, or 10, and print to terminal "Roll X resulted in a value
# of Y" where X is the # of rolls and Y is the value of the die.

from random import randint
from time import sleep

b_high_roll = False
i_roll_number = 0
while not b_high_roll:
    num = randint(1, 10)
    i_roll_number += 1
    if num >= 8:
        print("Roll", i_roll_number, "resulted in a value of", num)
        b_high_roll  = True
    else:
        print(num)
    sleep(.1)
