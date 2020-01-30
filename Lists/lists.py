'''
# Lists
append()   -  Adds an element at the end of the list
clear()	   -  Removes all the elements from the list
copy()	   -  Returns a copy of the list
count()	   -  Returns the number of elements with the specified value
extend()   -  Add the elements of a list (or any iterable), to the end of the current list
index()	   -  Returns the index of the first element with the specified value
insert()   -  Adds an element at the specified position
pop()	   -  Removes the element at the specified position
remove()   -  Removes the first item with the specified value
reverse()  -  Reverses the order of the list
sort()	   -  Sorts the list '''

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']

cars.sort()
print(cars)

def myFunc(e):
  return len(e)

cars.sort(key=myFunc)
print(cars)

cars.reverse()
print(fruits)


cars.remove("banana")
print(cars)
cars.remove("VW")
print(cars)

cars.pop()
print(cars)

cars.insert(1, "Hyundai")
print(cars)

print(cars.index('BMW'))

cars.extend(['volvo','benz'])
print(cars)

print(cars.count('Hyundai'))

temp = cars.copy()
print(temp)

a = ['Maruthi','Mahindra']
cars.append(a)
print(cars)

temp.clear()
print(temp)

