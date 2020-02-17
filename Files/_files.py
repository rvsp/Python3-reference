'''
Owner: Venkatasubramanian
Topic: Files
'''

'''
Basic operations:
1) Open a file
2) Read or write (perform operation)
3) Close the file

File modes
'r'     Open a file for reading. (default)
'w'     Open a file for writing. Creates a new file if it does not exist or truncates the file if it exists.
'x'     Open a file for exclusive creation. If the file already exists, the operation fails.
'a'     Open for appending at the end of the file without truncating it. Creates a new file if it does not exist.
't'     Open in text mode. (default)
'b'     Open in binary mode.
'+'     Open a file for updating (reading and writing)
'''

# open file
f = open("test.txt")
# f = open("file-path/filename.txt")

# read mode
f = open("test.txt",'r',encoding = 'utf-8')
print(f.read())

# write mode
with open("test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n\n")
   f.write("contains three lines\n")
