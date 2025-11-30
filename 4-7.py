import re
words = input('Speak. : ')
vowels = len(re.findall('[aeiouAEIOU]',words))
print(vowels)