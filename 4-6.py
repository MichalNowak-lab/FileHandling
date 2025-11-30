import re
plik = input('Enter file: ')
with open(plik,'r') as file:
    read_file= file.read()
    lines = read_file.split('\n')
words = len(re.findall('[a-zA-z_]+',read_file.replace('\n','')))
print(len(lines))
print(len(read_file.replace('\n','')))
print(words)