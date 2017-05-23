exampleString = 'hello World this is an awesome string'
# This string acts like an array in other languages. Some functions that you can do with this string.

#Finding the len of the string in python:
sLen = len(exampleString)

print(sLen)

#You can extract a certain char from the string using array notation
a = exampleString[2]

#print(a)

#Strings are immutable you can't change strings using this notation
#For example you can't do: exampleString[1] = 'b' This is not allowed by the interpreter

#You can slice strings using the [:] notation

b = exampleString[6:]

#print(b)

#Looping over a string

example = ''

for x in exampleString:
    example += x

#print(example)

#Example problem: Find the number of spaces in a string
counter = 0

for x in exampleString:
    if x == ' ':
        counter += 1

#print(counter)

#Since strings are immutable it is not possible to replace individual characters of a string
#To do that you will need to convert them to a list first

exampleList = list(exampleString)

#print(exampleList)

#Now you can manipulate the list. For example
exampleList[:5] = 'awesome'

#Convert back by changing list into a string again using the join method

#exampleString = "".join(exampleList)

#print(exampleString)

#Example problem. Capitalize the chars in the string.
exampleList[0] = exampleList[0].upper()

for x in range(sLen):
    if exampleList[x] == ' ' and x < sLen - 1:
        exampleList[x+1] = exampleList[x+1].upper()

exampleString = "".join(exampleList)

print(exampleString)

#Displaying strings using format
day = '23rd'
month = 'May'
year = '2017'

#If you want to display this like '23rd May 2017' an easy way is to use the format method
print('{day} {month} {year}'.format(day=day, month=month, year=year))
#print('{day} {month} {year}'.format_map(vars()))

#Some inbuilt useful string functions.
ex1 = 'awesome'
print(ex1.upper())

ex2 = 'AWESOME'
print(ex2.lower())

ex3 = 'i want this string to be capitalized'
print(ex3.capitalize())
