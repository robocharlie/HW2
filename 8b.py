# WRite a new python script that will read each line of text form the file in part(a) and sequentially print each line
# to the terminal with all spaces removed. in other words, if the file contains a line "ENME 489B is fun" the output
# should read "ENME489Bisfun". Hint: see the readline() method for files. Hint: you may need to check for both spaces
# and newline characters to make sure your output does not have extra blank lines.

try:
    file = open('8ainput.txt', 'r')
except FileNotFoundError:
    exit()

while True:
    file_line = file.readline()
    output_line = file_line.replace(' ', '')
    output_line = output_line.replace('\n', '')
    if not output_line:
        break
    print(output_line)

