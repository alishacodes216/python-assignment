# 1.   Creates a list of numbers from 1 to 10.
# 2.   Extracts the first five elements from the list.
# 3.   Reverses these extracted elements.
# 4.   Prints both the extracted list and the reversed list

list = [1,2,3,4,5,6,7,8,9,10]
five_element = list[:5]
reverse_element = five_element[::-1]
print(f'Extracted first five elements: {five_element}')
print(f'Reversed extracted elements :{reverse_element}')