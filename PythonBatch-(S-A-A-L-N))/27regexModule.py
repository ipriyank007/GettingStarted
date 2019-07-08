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
jjnjnjnkmkmkmkmkmkml,k,./748685[km l./[}|1723+
dh
er]]
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
13 Jan,1994
19/12:2025

16\\12\\1999
14-04-1994
12/11/2011

names:

Mr Priyank
Ms Vandana
Mr. Sumit
Ms. Priyanka

email ids:

priyank7137@gmail.com
v.negi@yahoo.co.uk
sumit.giri97@gmail.com
priyanka.sriv25@hotmail.com

'''

sentence = 'This is a simple sentence'

pattern = re.compile(r"\w+\.?(\w+)?@\w+\.\w+(\.\w+)?")
# pattern = re.compile(r"")

matches = pattern.finditer(target_text)


for match in matches:
    print(match)
