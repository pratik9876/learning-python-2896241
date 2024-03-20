# 
# Example file for variables
# LinkedIn Learning Python course by Joe Marini
#


# Basic data types in Python: Numbers, Strings, Booleans, Sequences, Dictionaries
myint = 5
myfloat = 13.2
mystr = "This is a string"
mybool = True
mylist = [0, 1, "two", 3.2, False]
mytuple = (0, 1, 2)
mydict = {"one" : 1, "two" : 2}

print(myint)
print(myfloat)
print(mystr)
print(mybool)
print(mylist)
print(mytuple)
print(mydict)

# print("____________")


# re-declaring a variable works
# myint = "abcd"
# print(myint)

# print("____________")

# to access a member of a sequence type, use []
print("_____list_______")
print(mylist[2])
print("_____tuple_______")
print(mytuple[2])





# use slices to get parts of a sequence
print(mylist[1:4:2])
# list[Start:End:Step]

# you can use slices to reverse a sequence
print(mylist[::])
print("_____reverse______")
print(mylist[::-1])

# dictionaries are accessed via keys
print(mydict["two"])

# ERROR: variables of different types cannot be combined
print(mystr + " : "+ str(myint))
# Global vs. local variables in functions

def someFunction():
    mystr = "def"
    print(mystr)

def someFunction1():
    global mystr
    mystr = "def"
    print(mystr)

someFunction()
print(mystr)
someFunction1()
print(mystr)

#deleting variables
del mystr
print(mystr)