import re

target_text = '''abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWZYZ
0123456789
https://www.google.com
http://www.yahoo.com
https://wikipedia.org

my contacts 

809 384 9242
900-234-3567
700*409*4589

These are some more texts.

You have to escape these:
. { } [ ] ( ) \ | ^ $ * + ?

Important regex metacharacters:

. - Any characters accept newline.
^ - Beginning of a string.
$ - End of a string.
\d - Digits(0-9)
\D - Non-Digits.
\w - Word Characters (a-z, A-Z, 0-9, _).
\W - Not a word character.
\s - White spaces (space, tab, newline).
\S - Non White spaces.
\b - Word boundary.
\B - Not a word boundary.

 
important dates

15/Aug/1994
13 Jan, 1994
19/12:2025

names:

Mr Priyank
Ms Vandana
Mr. Sumit
Ms. Priyanka

email ids:

priyank7137@gmail.com
v.negi@yahoo.com
sumit.giri97@gmail.com
priyanka.sriv25@hotmail.com

'''

sentence = 'This is a simple sentence'

# pattern = re.compile(r"https?://(www\.)?\w+\.\w+")
# pattern = re.compile(r"\b\w\w\w\w\b")
pattern = re.compile(r"\d\d(/| )\w+[,|/|:]\s?\d\d\d\d")
matches = pattern.finditer(target_text)

for match in matches:
    print(match)

