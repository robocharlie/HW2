# Write a custom function called factorial() to calculate and display x! (x factorial) when passed an integer x,
# and call it to show the 10! = 3628800. Note: do not use the existing math.factorial(x) maodule - you must
# create your own implementation of the factorial function.


def factorial(x):
    b = 1
    for a in range(1, x+1):
        b = b*a
    return b

print(factorial(10))
