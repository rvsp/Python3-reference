'''
Owner: Venkatasubramanian
Topic: Loops and Control statements
'''

'''
for loop
while, while else loops
break, continue, pass
'''

# for loop
for letter in 'Python':
   print('Current Letter :', letter)

fruits = ['banana', 'apple',  'mango']
for fruit in fruits:
   print('Current fruit :', fruit)

for index in range(len(fruits)):
   print('Current fruit :', index, fruits[index])

for index in range(2,10,2):
    print(index)

# understand the range() method increment in for loop and implement decrement

# while loop
count = 0
while (count < 9):
   print('The count is:', count)
   count = count + 1

# while else loop
while count < 5:
   print(count, " is  less than 5")
   count = count + 1
else:
   print(count, " is not less than 5")

# do..while is absence in python
# your task to implement do..while concept with while loop

## control statements
var = 10
# break
while var > 0:              
   print('Current variable value :', var)
   var = var -1
   if var == 5:
      break

# continue
while var > 0:              
   var = var -1
   if var == 5:
      continue
   print('Current variable value :', var)

# pass
for letter in 'Python': 
   if letter == 'h':
      pass
      print('This is pass block')
   print('Current Letter :', letter)