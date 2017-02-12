# Continually generate a pair of random integers x and y, each between 0 and 20, and print "x/y = z", where x is the
# value of x, y is value of y, and z is result of x/y. Make sure that your print has no spaces between x/y, and have
# 1 space on either side of the '=' (hint: you can use Python text formatting syntax to achieve this). Finally, use
# exception handling so that if division by zero occurs the coe prints "division by zero" and the loop stops.

from random import randint

while True:
    try:
        x = randint(0, 20)
        y = randint(0, 20)
        z = x/y
        print('{}/{} = {}'.format(x, y, z))
    except ZeroDivisionError:
        print('division by zero')
        break
