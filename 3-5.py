###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input('Username: ')
password = input('Password: ')

# pattern (criteria) for username and password
username_pattern = '[a-z]{8,}'
password_pattern = '([a-zA-Z]{8,}(\d)(_))'

# check if username and password are ok
username_match = re.match(username_pattern,username)
password_match = re.match(password_pattern,password)

# print results
if username_match and password_match:
   print(username, password)
else:
   print('try again')