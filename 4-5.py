import re
with open('email.txt', 'r') as mail:
    plik = mail.read()
pattern_sender = 'From:\s.*?<([^>]+)>'
pattern_recipent = 'To:.*?<([a-z.]+@[a-z.]+\.[a-z]{2,})>'
pattern_subject = 'Subject:\s*(.*)'
patern_body = '(?:\r?\n){2}([\s\S]*)'

def email_sender(text,pattern):
    szukaj = re.search(pattern,text)
    print(szukaj.group(1))

def email_recipent(text,pattern):
    szukaj = re.search(pattern,text)
    print(szukaj.group(1))

def email_subject(text,pattern):
    szukaj = re.search(pattern,text)
    print(szukaj.group(1))

def email_body(text,pattern):
    szukaj = re.search(pattern,text)
    print(szukaj.group(1))
#email_sender(plik,pattern_sender)
#email_body(plik,patern_body)
#email_subject(plik,pattern_subject)
#email_recipent(plik,pattern_recipent)