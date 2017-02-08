# As in the previous problem, generate random integers between 1 and 10, performing exactly 25 rolls. Each time the
# number is between 8-10 store the roll value in a list. After all 25 rolls are done, sequentially print each
# stored value in the list.

# import the random integer function
from random import randint

# initialize list
mylist = list()

# roll 25 times, if value is 8 or larger put into list
for a in range(1, 26):
    roll = randint(1, 10)
    if roll >= 8:
        mylist.append(roll)

# Print the list
print(mylist)