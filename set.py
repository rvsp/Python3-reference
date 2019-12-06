s = {"apple", "banana", "cherry"}
print(s)

for x in s:
  print(x)
print("banana" in s)
s.add("orange")
print(s)
s.update(["orange", "mango", "grapes"])
print(s)
print(len(s))
s.remove("banana")
print(s)
s.discard("banana")
print(s)
x = s.pop()
print(x)
print(s)
s.clear()
print(s)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
set1.update(set2)
print(set1)
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
z = x.intersection(y)
print(z)
x.intersection_update(y)
print(x)

x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y)
print(z)

x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)