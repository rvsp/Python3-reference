import re
s = "tim email is tim@somehost.com"
match = re.search(r'[\w.-]+@[\w.-]+', s)

# the above regular expression will match a email address

if match:
    print(match.group())
else:
    print("match not found")


s1 = "Tim's phone numbers are 12345-41521 and 78963-85214"
match = re.findall(r'\d{5}', s1)

if match:
    print(match)


m = "python tuts"
match = re.match(r'py', m)
if match:
    print(match.group())

match = re.search(r'^py', m)
if match:
    print(match.group())


sr = "The rain in Spain"
x = re.split("\s", sr)
print(x)

ss = "The rain in Spain"
x = re.sub("\s", "9", ss, 2)
print(x)


string = '\n and \r are escape sequences.'
result = re.findall(r'[\n\r]', string) 
print(result)

x = 'We just received $10.00 for cookies.'
y = re.findall('\$[0-9.]+',x)
print(y)


mail="abc@gmail.com"
if(re.search(r'^\S@', mail)):
    print('true')
else:
    print('false')
