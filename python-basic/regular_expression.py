'''
    Date  : 19/10/2020
    Day   : Monday
    Author: Md. Aminul Islam
    Topic : Regular Expression
'''

import re

pattern = r"Bangla"

# result = re.match(pattern, "Bangladesh")

# if result:
#     print("Matched")
# else:
#     print("NO Match")

if re.search(pattern, "There is a country named Bangladesh in South Asia"):
    print("Match Found")
else:
    print("No match Found")

print(re.findall(pattern, "Bangladeshi Bangla and Indian Bangla are different."))


## some methods of return object's
pattern = r"bin"
match = re.search(pattern, "combination")

if match:
    print(match.group())
    print(match.start())
    print(match.end())
    print(match.span())


## Meta Character
pattern = r"^wr.te$"

if re.match(pattern, "write"):
    print("Match 1")
if re.match(pattern, "wrote"):
    print("Match 2")
if re.match(pattern, "writter"):
    print("Match 3")

## Character Class
# pattern = r"[,.]"
# user_input = input("Enter your number: ")
# print(re.split(pattern,user_input))
# print("\n".join(re.split(pattern,user_input)))


## Character range match
patterns = r"[A-Z][A-Z][0-9]"
match1 = re.search(patterns, "NS1 is prefix of first name")
if match1:
    print(match1.group())

pattern2 = r"[^A-Z][A-Z][0-9]"
match2 = re.search(pattern2, "nS1 is prefix of first name")
if match2:
    print("match")


## group
pattern  = r"egg(spam)*"

if re.match(pattern, "egg"):
    print("match1")

if re.match(pattern, "eggspamspamspamegg"):
    print("Match 2")

if re.match(pattern, "spam"):
    print("Match 3")

pattern = r"a(bc)(de)(f(g)h)i"

match = re.match(pattern, "abcdefghijklmnop")
if match:
    print(match.group())
    print(match.group(0))
    print(match.group(1))
    print(match.group(2))
    print(match.groups())
