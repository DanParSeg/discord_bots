

#regex: roman numbers
from re import search

def is_roman_number(s):
  if(len(s)==0):
    return False
  s=s.upper()
  return search("^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", s)

def roman_to_int(s):
  s=s.upper()
  roman = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
  i = 0
  num = 0
  while i < len(s):
     if i+1<len(s) and s[i:i+2] in roman:
        num+=roman[s[i:i+2]]
        i+=2
     else:
        #print(i)
        num+=roman[s[i]]
        i+=1
  return num


def is_count_msg(msg):
  msg=msg.strip()
  if(msg.isdigit()):
    return True
  return False




