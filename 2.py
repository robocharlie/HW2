# Using nested for loops, count a variable x from 1 to 5, and for each value x in the count,
# calculate the sum from 1 to x, printing each result


for x in range(1, 6):
    print(sum(range(1, x+1)))
