import re
import os
import collections

title = input("Title of text file <title>.txt: ")
f = open('texts/%(title)s.txt' % locals(),'r', encoding="utf-8") #text of title
o = open('texts/%(title)s_characters.txt' % locals(),'w+') #matches
text = f.read()

matches = re.findall(r"(?<=[A-Za-z] )\b[A-Z][a-z]+\b(?:(?:. | )[A-Z][a-z]+\b)?", text) 
# general novel (only matching capital letters that follow a word)

#matches = re.findall(r"(?<=\n)\b[A-Z]+\b(?: [A-Z]+\b)?(?=\n)", text) 
#shakespearean formatted play

names = dict()
for match in matches:
	names[match] = names.get(match, 0) + 1
names = collections.OrderedDict(sorted(names.items(), key=lambda t: t[1], reverse=True))

for name in names:
	o.write(name + ": " + str(names[name]) + "\n")
o.seek(0, os.SEEK_SET)
print(o.read())