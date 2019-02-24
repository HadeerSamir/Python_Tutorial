""" Python is used for:
######################
 web development (server-side),software development,mathematics,system scripting."""

""" What can Python do?
######################
 Python can be used on a server to create web applications.
 Python can be used alongside software to create workflows.
 Python can connect to database systems. It can also read and modify files.
 Python can be used to handle big data and perform complex mathematics.
 Python can be used for rapid prototyping, or for production-ready software development. """

""" to run a python file either make a file and run the command ( python fileName ) or open the command line as editor 
 and write the python code ( python ) open the cmd as editor and to exit the cmd from the python mode type ( exit() ). """

 #### IMPORTANT ######

 #    The any() method returns True if any element of an iterable is True. If not, any() returns False. such as print (any())
 #    To print items in one line using separator without using string menthods use ( print(item,end="separator") ).

print("Hello,World!")

""" Python Indentations 
######################
 python uses indentations to define a block of code don't use curly brackets as any programmong language."""

if 5>3:
	print("Five is greater than three")

# Comments Sample ( # ) for single line comment or ( """ """)Docstrings for multiline comment.

###########################################################################################################

""" Python Variables
##################
- python msh zay l programming languages l tanya n lazm a3ml declaration ll variable l awel b3d keda a assign 
l value ll variable l2 na 3la tol b assign l value ll variable mn 8eer ma a3ml declaration w kman msh b7tag a7ded type
mo3en ll variable na kman momkn b3d ma assign integer value ll variable assign leh string value w a8er l type bta3o.
- to combine a text to a variable use ( + ) sample for Strings ONLY ."""

x = 5
y = "Hello"
z = 7
w = 3
# print(" x = " + x)    ERROR L comination for strings only
print(" y = " + y)
x = "Hello x"
print(" New x = " + x)
print(w+z)

############################################################################################################

""" Python Numbers
################
There is 3 types of numbers in python ( int , float , complex ) w 3shan at check l type bta3 l variable
bst5dem ( type(variableName) )"""

x0 = 1
x1 = 2.7
x2 = 3E3    # float
x3 = 34e2   # float
x4 = 2j

print(type(x0))
print(type(x1))
print(type(x2))
print(type(x3))
print(type(x4))

# Python Casting ( int() , float() , str() )
#################

x5 = int(x1)
x6 = int("3") # hy7walha l int
x7 = float(x0)
x8 = str(x0)
print(x5)
print(x6)
print(x7)
print(x8,type(x8))

#############################################################################################################

"""Python String
################
- value of string surrounded by (' ') or (" "). 
- python don't have character datatype so string is an array of bytes representing unicode characters.
- use [] to access elements of string.
- to get a substring use [start:end].
- to remove a whitespaces from the begining or end of string use ( stringName.strip() ).
- to get the length of the string ( len(stringName) ).
- to get the string in lower case use ( stringName.lower() ).
- to get the string in upper case use ( stringName.upper() ).
- to replace a character with a character in string use ( stringName.replace(old,new) ).
- to split a string to substrings according to a separator use ( stringName.split("separator")).
- to ask a user to enter an input use ( variableName = input()) .
- String Methods ( stringName.isalnum() This method checks if all the characters of a string are alphanumeric (a-z, A-Z and 0-9)
  stringName.isalpha() This method checks if all the characters of a string are alphabetical (a-z and A-Z).
  stringName.isdigit() This method checks if all the characters of a string are digits (0-9)).
- ( stringName.ljust(width) ) This method returns a left aligned string of length width.
- ( stringName.center(width) ) This method returns a centered string of length width.
- ( stringName.rjust(width) ) This method returns a right aligned string of length width.
- The textwrap module provides two convenient functions: wrap() and fill().

textwrap.wrap() 
The wrap() function wraps a single paragraph in text (a string) so that every line is width characters long at most. 
It returns a list of output lines.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.'] 
textwrap.fill() 
The fill() function wraps a single paragraph in text and returns a single string containing the wrapped paragraph.

>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.

"""

s0 = " Learning,Python   "
print(s0)
print(s0[1]) # e
print(s0[1:7])  # [1:7[
print(s0.strip())   # remove whitespaces from begin and end 
print(len(s0))
print(s0.lower())
print(s0.upper())
print(s0.replace("L","$"))
print(s0.split(","))
print(s0[0])
print("Enter Your Name : ")
#s1 = input()
#print("Hello",s1)


##################################################################################################

""" Python Operators
#####################
- Arithmatic Operators ( + , - , * , / , % , ** (Power or Exponentiation) , // (floor) ).
- Assignment Operators ( = , += , -= , *= , /= , %= , //= , **= , &=  , |= , ^= , >>= , <<= ).
- Comparsion Operators ( == , != , < , > , <= , >= ).
- Logical Operators ( and , or , not() ).
- Identity Operators ( is ,  is not ) is m3naha n 2 variables lehon nfs l id .
- Membership Operators ( in , not in ).
- Bitwise Operators ( & , | , ^  (XOR) , ~ (NOT) , << (ZERO FILL LEFT SHIFT) , >> (SIGNED RIGHT SHIFT)). 
"""
s2 = 3
s2 **= 2   #power

"""    s3 = 5
       s3 ^= 3
       print(s3)
       s4 = 5
	   s4 >>= 3           ********check*************
       print(s4)
       s5 = 5
	   s5 <<= 3
       print(s5)
  """

print(x)
print(10//3)
print(10**3) 
print(s2)

s6 = 9
s7 = 9
print(id(s6),id(s7))
print(s6 is s7)
print(s6 is not s7)  # return true although n lehom nfs l content lkn l object mo5tlf   *******CHECK***********

s8=["A","B","C"]
print("A" in s8)
print("D" not in s8)

###############################################################################################################

""" Python Collections (Arrays)
##############################
- There are 4 types of collections in python :	list , tuple , set , dictionary.
"""

"""List
########                                                  *********************  check extend() ********************
- is a collection which is ordered and changeable.
- Allows duplicate members.
- Writting using [].
- access of items using listName[index] starting from zero.
- you can loop through a list using for loop.
- to get length of the list use ( len(listName) ).
- to add item to the end of the list use ( listName.append(item) ).
- to add item to a certain position in the list use ( listName.insert(position,item) ).
- to remove an item from the list use ( listName.remove("elementName") ).
- to remove a specified element or if not specified remove the last element of the list use ( listName.pop() ).
- to remove a specified element use ( del listName[index]) and if we don't specify the index it will remove
all the elements of the list.
- to emptize the list use ( listName.clear() ).
- we can make a list using list constructor ( listName = list(("apples", "B","c")) ).
- list methods ( copy() [ make a copy of the list] , count() [ returns the number of the elements of specified value] ,
extend() [Add the elements of a list (or any iterable), to the end of the current list] , 
index() [Returns the index of the first element with the specified value] , reverse() [Reverses the order of the list]
, sort() [sort the list])
"""

thisList = ["apple" , "orange" , "banna"]
print(thisList)
print(thisList[0])
thisList[0] = "mango"
print(thisList)

for x in thisList:
	print(x)

if "mango" in thisList:
	print("EXISTS")

print(len(thisList))

thisList.append("apple")
print(thisList)

thisList.insert(0,"stropary")
print(thisList)

thisList.remove("apple")
print(thisList)

thisList.pop()
print(thisList)

thisList.pop(1)
print(thisList)

del thisList[0]
print(thisList)

#del thisList
#thisList.clear()
#print(thisList)

thisList1=list(("A","B","C"))
print(thisList1)

""" Tuples
############
- is a collection which is ordered and unchangeable. Allows duplicate members.
- is written using ().
- to access elements of the tuple use ( tupleName[index] ).
- to loop through the tuple use ( for loop ).
- check if item exits in the tuple use ( in ).
- to get the tuple length use ( len(tupleName) ).
- since tuple is not changeable we cannot add or remove items to it.
- to delete the tuple completely use ( del tupleName ).
- we can define a tuple using tuple constructor ( tupleName = tuple(("A","B","C"))).
- tuple methods ( count() [ Returns the number of times a specified value occurs in a tuple ] , 
index() [ Searches the tuple for a specified value and returns the position of where it was found]).
"""

thisTuple = ("A","B","C")
print(thisTuple)
print(thisTuple[0])
#thisTuple[0]="F"
#print(thisTuple)  # DON'T CHAMGE Hytl3 error
for x in thisTuple:
	print(x)

if "A" in thisTuple:
	print("EXISTS")

print(len(thisTuple))

#thisTuple[3] = "L"  # Error

del thisTuple
# print(thisTuple)   htl3 error 3shan l tuple da 5las atmas7 mb2ash mwgod 

thisTuple1=tuple(("D","E","F","D"))
print(thisTuple1)

count=thisTuple1.count("D")
print(count)

index=thisTuple1.index("D")
print(index)

"""Sets
########
- is a collection which is unordered and unindexed.
- No duplicate members.
- is written using {}.
- You cannot access items in a set by referring to an index, since sets are unordered the items has no index.
- But you can loop through the set items using a for loop, or ask if a specified value is present in a set, 
by using the in keyword.
- Once a set is created, you cannot change its items, but you can add new items using ( setName.add(item) ) and 
you can add more than one item to a set use ( update([item1,item2,.....]) ).
- to get the length of the set use ( len(setName) ).
- to remove an item from the set use ( setName.remove(item) or setName.discard(item) ) lw l element l 3ayza
amsa7a msh mwgod w ast5dmt remove() htl3 error lkn discard msh htl3 error.
- You can also use the pop(), method to remove an item, but this method will remove the last item. 
Remember that sets are unordered, so you will not know what item that gets removed.and the return value of it is 
the removed element.
- to emptize the set use ( setName.clear() ).
- to delete the set completely use ( del setName ).
- to create a set using constructor use ( setName = set(("A","B")) ).
- Set methods ( copy() [Returns a copy of the set] , 
difference() [Returns a set containing the difference between two or more sets] , 
difference_update() [removes the items in this set that are also included in another, specified set] , 
intersection() [ Returns a set, that is the intersection of two other sets ] , 
intersection_update() [Removes the items in this set that are not present in other, specified set(s)] )

"""

thisSet={"A","B","C"}
print(thisSet)              #NOTE : Sets are unordered, so the items will appear in a random order y3nii kol print b 
							# output mo5tlf

for x in thisSet:
	print(x)

if "C" in thisSet:
	print("EXISTS")

thisSet.add("D")
print(thisSet)

thisSet.update(["E","F","G"])
print(thisSet)

print(len(thisSet))

z = thisSet.pop()
print(z)  

'''
x = {"apple", "banana", "cherry"}                 ********CHECK*************
y = {"google", "microsoft", "apple"}

z = x.difference(y) 
print(z)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

x.difference_update(y) 

print(x)
'''

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y) 

print(z)


'''Dictionary
#############
- is a collection which is unordered, changeable and indexed.
- No duplicate members.
- dictionaries are written with curly brackets, and they have keys and values.
- to access the items of the dictionary use ( dictionaryName["KeyName"] or dictionaryName.get("keyName") ).
- you can loop through the dictionary using for loop .
- to get the value of the dictionary use ( dictionaryName.values() ).
- to loop through key and value in the same time use ( dictionaryName.items() ).
- to check if the certain key exists in the dictionary use ( in ).
- to get the dictionary length use ( len(dictionaryName) ).
- to add item to the dictionary use ( dictionaryName["newKey"] = value ).
- to remove item from the dictionary use ( dictionaryName.pop("keyName")  or dictionaryName.popitem() w d btmsa7 random item
or remove the last item or del dictionaryName["keyName"] ).
- to delete the dictionary completely use ( del dictionaryName ).
- to emptize the dictionary use ( dictionaryName.clear() ).
- you can create a dictionary using constructor ( dictionaryName = dict(key=value,.......) )

'''

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict)
print(thisdict["brand"])
print(thisdict.get("model"))
thisdict["year"] = 2019 
print(thisdict)

for x in thisdict:   
	print(x)             # print key
	print(thisdict[x])   # print value

for x in thisdict.values():
	print(x)

for x,y in thisdict.items():
	print(x,y)

if "brand" in thisdict:
	print("EXISTS")

print(len(thisdict))

thisdict["price"]=300000
print(thisdict)

thisdict.pop("price")
print(thisdict)

thisdict.popitem()
print(thisdict)

del thisdict["model"]
print(thisdict)

del thisdict
#print(thisdict)  # htl3 error 3shan l variable da mb2ash mwgod asln

thisdict1 = {"key1":1,"key2":2}
print(thisdict1)
thisdict1.clear()
print(thisdict1)

thisdict2 = dict(key1=1,key2=2)
print(thisdict2)

###############################################################################################

'''IF-ELSE ( IF , ELSE IF = elif ,  )
###########
'''

a = 33
b = 200
if b > a:
  print("b is greater than a")

#print("B")if b>a else print("A")


a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

if a>b and a>100:
	print("A")

if a>b or a>100:
	print("A")

#################################################################################################

# While & For $ Range  & For Else Loop and Break statement and continue statement.
######################################################################################
# l for else feha l else bttnfaz lma l for finished

i=1
while i<10:
	if i==3:
		break
	print(i)
	i+=1

i=1
while i<10:
	i+=1
	if i==3:
		continue
	print(i)

for x in "banana":
	print(x)

# range(start,end,step)
for x in range(6):  # from 0 to 6 step by 1 [0,6[
	print(x)

for x in range(1,10):
	print(x)

for x in range(1,10,2):
	print(x)

for x in range(6):
  print(x)
else:
  print("Finally finished!")


adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

#################################################################################################

'''Python Functions
##################
- In Python a function is defined using the ( def ) keyword.
- To call a function, use the function name followed by parenthesis.
- You can add default parameter value to a function.In this case if we call the function without passing value to it it will
 use the default value.
 - to let a function return a value, use the return statement.
 - Python also accepts function recursion, which means a defined function can call itself
'''

def printHello():
	print("Hello World")

printHello()

def printFirstName(firstName):
	print("HELLO "+firstName)

printFirstName("Hadeer")

def defaultValueFunction(firstName = "Hadeer"):
	print("Hello From Default "+firstName)

defaultValueFunction()

def myFunction(x):
	return 5*x

y = myFunction(5)
print(y)

def tri_recursion(k):                                         # **********************CHECK************************
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(6)


##############################################################################################################

'''Python Lambda 
################
- A lambda function is a small anonymous function ( that don't have name and its body has one line only but can has any number
of parameters).
- syntax  ( lambda arguments : expression) the expression is executed and the value is returned.
- The power of lambda is better shown when you use them as an anonymous function inside another function.
- Use lambda functions when an anonymous function is required for a short period of time.
'''

x = lambda a : a+10
print('\n')
print(x(5))

x0 = lambda a,b : a*b
print(x0(2,3))

def myfunc(n):
  return lambda a : a * n

x1 = myfunc(2)
print(x1(4))

###########################################################################################################

'''Python Arrays
#################
- Python does not have built-in support for Arrays, but Python Lists can be used instead.
- Arrays are written using [].
- to access the value of the array use ( arrayName[index] ).
- to get the length of the array use ( len(arrayName) ).
- to loop through the array use ( for in loop ).
- to add element to the array use ( arrayName.append(value) ).
- to remove an element from the array use ( arrayName.pop(index) or arrayName.remove(value) 
 remove() method only removes the first occurrence of the specified value).
'''
