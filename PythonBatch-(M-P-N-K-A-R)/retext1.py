import re

target_text= '''
    
    12 jan 2019
12/06/1998
22-10-2013
5 July, 2018

'''

#pattern = re.compile("\d\d[-]\w\w[-]\d\d\d\d")
pattern = re.compile("\d\d?( |/|-)(\d\d)|(\w+)[ |/|,] ?\d\d\d\d")
matches = pattern.finditer(target_text)

for match in matches:
    print(match)
