'''
Owner: Venkatasubramanian
Topic: Sets
'''

s = {"apple", "banana", "cherry"}
print(s)

for x in s:
  print(x)
print("banana" in s)

# add element to set
s.add("orange")
print(s)

# update set with union of this set and others
s.update(["orange", "mango", "grapes"])
print(s)
print(len(s))
s.remove("banana")
print('remeove',s)

# removed specified item
s.discard("apple")
print('discard',s)
x = s.pop()
print(x)
print(s)
s.clear()
print(s)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
# returns set contain the union of set
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)
# note the double round-brackets
thisset = set(("apple", "banana", "cherry")) 
print(thisset)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# returns set contain difference of two or more
z = x.difference(y)
print(z)

# returns intersection of other two set
z = x.intersection(y)
print(z)

# remove the items that are present in other
x.intersection_update(y)
print(x)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

# check whether set contains or not
z = x.issubset(y)
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}

# return set contain another set or not
z = x.issuperset(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# symmetric difference of two sets
z = x.symmetric_difference(y)
print(z)