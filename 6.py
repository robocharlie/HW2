# As in the previous problem, generate random integers between 1 and 10, performing exactly 25 rolls. EAch time the
# number is between 8-10 store the corresponding attempt number and roll value in a dictionary. After the 25 rolls are
# done, print "Roll X resulted in a value of Y" for each case where the result was 8, 9, or 10.

from random import randint

rolls = {}

for x in range(1,26):
    num = randint(1,10)
    if num >= 8:
        rolls[x] = num

for key in rolls:
    print('Roll {} resulted in a value of {}'.format(key,rolls[key]))
