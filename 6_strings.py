'''
Owner: Venkatasubramanian
Topic: Strings
'''

from string import maketrans
import string

s='i love proram'

if len(s)<= 100:
    print(s)


s='Checking the network cables'
s1= 'modem and router'


print(len(s))                  # return length of string
print(s1.capitalize())         # Converts first character to Capital Letter
print(s1.title())              # Returns a Title Cased String
print(s.center(80,' '))        # Pads string with specified character
print(s.startswith('Ch',2,10)) # Checks if String Starts with the Specified String
print(s1.endswith('r'))        # Checks if String Ends with the Specified Suffix
print(s.isalnum())             # Checks Alphanumeric Character
print(s.isalpha())             # Checks if All Characters are Alphabets
print('343434'.isdigit())      # Checks Digit Characters
print(s1.find('e',2,10))       # Returns the index of first occurrence of substring
print(s.islower())             # Checks if all Alphabets in a String are Lowercase
print('SDFSDF'.isupper())      # returns True if all characters are uppercase
print(s.isnumeric())           # Checks Numeric Characters
print(s1.lower())              # returns lowercased string
print(s1.upper())              # returns uppercased string
print(s.swapcase())            # swap uppercase characters to lowercase; vice versa
print(s.isspace())             # Checks Whitespace Characters
print(s.istitle())             # Checks for Titlecased String
print(s.count('e',4,8))        # returns occurrences of substring in string
print(s1.zfill(70))            # Returns a Copy of The String Padded With Zeros
print(s1.replace('e','%',2))   # Replaces Substring Inside
print(s.rstrip('*'))           # Removes Trailing Characters
print(s.lstrip('*'))           # Removes Leading Characters
print(s1.rjust(100,'^'))       # returns right-justified string of given width
print(s1.ljust(50,'#'))        # returns left-justified string of given width
print(s.split())               # split and returns value in list type


i ,o = 'aeiou', '12345'
tr=maketrans(i,o)              # returns a translation table
print(s1.translate(tr))        # returns mapped charactered string