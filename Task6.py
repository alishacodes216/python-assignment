# Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# -Square root of the number
# -Natural logarithm (log base e) of the number
# -Sine of the number (in radians)
# Displays the calculated results.

import math
num=float(input('enter number:'))
print(f'square root {math.sqrt(num)}')
print(f'log is {math.log(num)}')
print(f'sine is {math.sin(num)}')