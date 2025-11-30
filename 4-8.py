import re
with open('files.txt','r') as file:
    red = file.read()
    red = red.split('\n')
for line in red:
    if re.match('.*\.[a-z]{4}',line):
        print(line)