'''
Owner: Venkatasubramanian
Topic: Dictonary
'''

'''
copy()	        Returns Shallow Copy of a Dictionary
fromkeys()	    creates dictionary from given sequence
get()	        Returns Value of The Key
items()	        Returns view of dictionary's (key, value) pair
keys()	        Returns View Object of All Keys
setdefault()	Inserts Key With a Value if Key is not Present
values()	    returns view of all values in dictionary
update()	    Updates the Dictionary
popitem()	    Returns & Removes Element From Dictionary
pop()	        Removes and returns element having given key
clear()	        Removes all Items
'''

my_dict = {}
print(my_dict)

my_dict = {1: 'apple', 2: 'ball'}
print(my_dict)

my_dict = {'name': 'John', 1: [2, 4, 3]}
print(my_dict)

my_dict = dict({1:'apple', 2:'ball'})
print(my_dict)

my_dict = dict([(1,'apple'), (2,'ball')])
print(my_dict)

se = ('name','age','address')
d = dict.fromkeys(se)
print(d)

my_dict = {'name':'Jack', 'age': 26}

print(my_dict['name'])
print(my_dict.get('age'))

temp = my_dict.copy()
print(temp)

#removed in python3
#print(my_dict.has_key('age'))

print(my_dict.items())

print(my_dict.keys())

my_dict.setdefault('mobile',None)
print(my_dict)

temp_d = {'email':'abc@gmail.com'}
my_dict.update(temp_d)
print(my_dict)

print(my_dict.values())

result = my_dict.popitem()
print(result)

res = my_dict.pop('age')
print(res)
print(my_dict)

my_dict.clear()
print(my_dict)