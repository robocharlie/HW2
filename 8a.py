# Using the knowledge from the lynda tutorial 4.1, write a python script that will create a new text file, use the
# input() function to continuously request lines of text from the user, and write each entered line to the file,
# stopping only when the user enters a null line (by hitting return without entering any text). The program should
#  terminate at this point. Hint: be sure to add a newline character '\n' to each line written to the file.


file = open("8aInput.txt", "w+")

while True:
    user_input = input()
    if not user_input:
        break
    else:
        file.write(user_input)
        file.write('\n')
