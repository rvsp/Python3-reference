'''
Owner: Venkatasubramanian
Topic: Python array module
'''

import array as arr

a = arr.array('d', [1.1, 3.5, 4.5])
print(a)

a1 = arr.array('i', [2, 4, 6, 8])
print("First element:", a1[0])
print("Second element:", a1[1])
print("Last element:", a1[-1])

# slice in array
numbers_list = [2, 5, 62, 5, 42, 52, 48, 5]
numbers_array = arr.array('i', numbers_list)
print(numbers_array[2:5]) # 3rd to 5th
print(numbers_array[:-5]) # beginning to 4th
print(numbers_array[5:])  # 6th to end
print(numbers_array[:])   # beginning to end

# change or add values
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])
numbers[0] = 0    
print(numbers)
numbers[2:5] = arr.array('i', [4, 6, 8])   # changing 3rd to 5th element
print(numbers)

# append
appnd = arr.array('i', [1, 2, 3])
appnd.append(4)
print(appnd)
appnd.extend([5, 6, 7]) 
print(appnd)

# +
odd = arr.array('i', [1, 3, 5])
even = arr.array('i', [2, 4, 6])
ar1 = arr.array('i')
ar1 = odd + even
print(ar1)

#remove or delete
rmv = arr.array('i', [1, 2, 3, 3, 4])
del rmv[2]
print(rmv)
del rmv
print(rmv)
rmv.remove(12)
print(rmv)
print(rmv.pop(2))
print(rmv)