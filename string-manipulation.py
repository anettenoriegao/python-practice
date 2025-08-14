string1 = 'This is a valid string'
string2 = "This is a valid string"

# Using the other quote for the nested quote
string3 = "'Always look on the bright side of life,' he said."

# Using escaped quotes for the nested quotes
string4 = "\"Always look on the bright side of life,\" he said."

print(string3)
print(string4)
print(len(string4))

filepath = '        /var/www/java/packages/are/too/long/here'
print(filepath)
filepath = filepath.strip()
print(filepath)
folders = filepath.split('/')
print(folders)
print(type(folders))

windowsPath = "\\".join(folders)
print(windowsPath)

multi = '''
Now this is a story all about how
My life got flipped turned upside down'''
print(multi)
multi.splitlines()
print(multi.splitlines)