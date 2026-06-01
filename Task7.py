# Write a Python program that:
# 1.   Opens and reads a text file named sample.txt.
# 2.   Prints its content line by line.
# 3.   Handles errors gracefully if the file does not exist.

try :
    with open('sample.txt','w') as file:
        data = file.write('1. This is a simple text file. \n2. It contains multiple items.')
        print(data)

    with open('sample.txt','r') as file:
        for line in file:
            print(line)
except FileNotFoundError:
    print('the file sample.txt not found')