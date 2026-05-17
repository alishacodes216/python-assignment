# 5. Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial
# using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.

def factorial():
    n=int(input('enter a number:'))
    fact=1
    for i in range(1,n+1):
        fact = fact * i
    return fact
res=factorial()
print(f'factorial is {res}')