'''
Owner: Venkatasubramanian
Topic: Operators
'''

'''
Arthmetic   ->  +, -, *, /, **, //, %
Assignment  ->  +=, -=, *=, /=, **=, //=, %=
Relational  ->  <, >, <=, >=, ==, !=
Logical     ->  and, or, not
Membership  ->  in, not in
Identity    ->  is, is not
Bitwise     ->  <<, >>, &, |, ^, ~
'''


# Arthmetic
printt(5+6, 5-3, 3*2, 3**2, 5/3, 5//3, 5%2)

# Assignment
c = 1
# c =c + 10
c += 10
print(c)

# Relational & Logical
a,b=5,10
print(a<b and a!=0)


# Membership
print(5 in [2,3,4,5,6,7])
print(1 in [2,3,4,5,6,7])
print(1 not in [2,3,4,5,6,7])

# Identity
print(5 is [2,3,4,5,6,7])
print(5 is not [2,3,4,5,6,7])

print([2,3,4,5,6,7] is [2,3,4,5,6,7])
print([2,3,4,5,6,7] is not [2,3,4,5,6,7,8])


# Bitwise
a=60
b=13
c=0
print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)