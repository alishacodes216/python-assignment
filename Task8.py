# Write a Python program that:
# 1.   Takes user input and writes it to a file named output.txt.
# 2.   Appends additional data to the same file.
# 3.   Reads and displays the final content of the file.

with open('output.txt','w') as file:
    user = input('enter text to write to the file: ')
    file.write(user)
print('Data sucessfully written in output.txt!')
with open('output.txt','a') as file:
    user = input('enter additional text to append: ')
    file.write(user)
print('Data sucessfully appended!')
with open('output.txt','r') as file:
    print('final content of output.txt: \n')
    content = file.read()
    print(content)