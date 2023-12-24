# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.0
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# +
# Study: Python Data Types
# https://www.tutorialspoint.com/python/python_data_types.htm

# Computer is a data processing device. 
# Computer stores the data in its memory and processes it as per the given program. Data is a representation of facts about a certain object.
# 컴퓨터는 데이터 처리 장치입니다. 컴퓨터는 데이터를 메모리에 저장하고 주어진 프로그램에 따라 처리합니다. 데이터는 특정 객체에 대한 사실을 표현한 것입니다.

# Data type represents a kind of value and determines what operations can be done on it. Numeric, non-numeric and Boolean (true/false) data are the most obvious data types. However, each programming language has its own classification largely reflecting its programming philosophy.

### Python Data TypesNumeric - int, float, complex
# Python has various built-in data types which we will discuss with in this tutorial:
# String - str
# Sequence - list, tuple, range
# Binary - bytes, bytearray, memoryview
# Mapping - dict
# Boolean - bool
# Set - set, frozenset
# None - NoneType

## =>  Number   |   Set   |   Dictionary   |   Sequence
#   => Intger                                 => String
#    => Boolean                               => List 
#   => Float                                  => Tuple
#    => Complex

## Python Numeric Data Type
# integer variable.
a=100
print("The type of variable having value", a, " is ", type(a))

# boolean variable.
b=True
print("The type of variable having value", b, " is ", type(b))

# float variable.
c=20.345
print("The type of variable having value", c, " is ", type(c))

# complex variable.
d=10+3j
print("The type of variable having value", d, " is ", type(d))


## Python Sequence Data Type
# Sequence is a collection data type.
# It is an ordered collection of items. Items in the sequence have a positional index starting with 0.
# It is conceptually similar to an array in C or C++. There are following three sequence data types defined in Python.
# => String Data Type
# => List Data Type
# => Tuple Data Type
# (Python sequences are bounded and iterable - Whenever we say an iterable in Python, it means a sequence data type (for example, a list).)

# Python String Data Type
str = 'Hello World!'
print('TutorialsPoint')
print("TutorialsPoint")
print('''TutorialsPoint''')
print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string
print(type(str)) # Prints concatenated string

# Python List Data Type
# Python 목록은 가장 다양한 복합 데이터 유형입니다.
# A Python list contains items separated by commas and enclosed within square brackets ([]). To some extent, Python lists are similar to arrays in C.
# One difference between them is that all the items belonging to a Python list can be of different data type where as C array can store elements related to a particular data type.
# 이들 사이의 한 가지 차이점은 Python 목록에 속하는 모든 항목은 C 배열이 특정 데이터 유형과 관련된 요소를 저장할 수 있는 다른 데이터 유형일 수 있다는 것입니다.
type([2023, "Python", 3.11, 5+6j, 1.23E-4])

# A list can have items which are simple numbers, strings, tuple, dictionary, set or object of user defined class also.
# >>> [['One', 'Two', 'Three'], [1,2,3], [1.0, 2.0, 3.0]]

list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']

print (list)            # Prints complete list
print (list[0])         # Prints first element of the list
print (list[1:3])       # Prints elements starting from 2nd till 3rd 
print (list[2:])        # Prints elements starting from 3rd element
print (tinylist * 2)    # Prints list two times
print (list + tinylist) # Prints concatenated lists

# Python Tuple Data Type
# Python tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parentheses (...).
# A tuple is also a sequence, hence each item in the tuple has an index referring to its position in the collection. The index starts from 0.
type((2023, "Python", 3.11, 5+6j, 1.23E-4))
# As in case of a list, an item in the tuple may also be a list, a tuple itself or an object of any other Python class.
print((['One', 'Two', 'Three'], 1,2.0,3, (1.0, 2.0, 3.0)))

# The main differences between lists and tuples are:
#  => Lists are enclosed in brackets ( [ ] ) and their elements and size can be changed
#  => .ie lists are mutable, while tuples are enclosed in parentheses ( ( ) ) and cannot be updated (immutable).
#  => Tuples can be thought of as read-only lists. For example −
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple)               # Prints the complete tuple
print (tuple[0])            # Prints first element of the tuple
print (tuple[1:3])          # Prints elements of the tuple starting from 2nd till 3rd 
print (tuple[2:])           # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2)       # Prints the contents of the tuple twice
print (tuple + tinytuple)   # Prints concatenated tuples


## Python Dictionary Data Type
#  Python dictionaries are kind of hash table type.
#  A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.
#  Python dictionary is like associative arrays or hashes found in Perl and consist of key:value pairs. The pairs are separated by comma and put inside curly brackets {}. To establish mapping between key and value, the semicolon':' symbol is put between the two.
dict = {}
dict['one'] = "This is one"
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}


print (dict['one'])       # Prints value for 'one' key
print (dict[2])           # Prints value for 2 key
print (tinydict)          # Prints complete dictionary
print (tinydict.keys())   # Prints all the keys
print (tinydict.values()) # Prints all the values

# Python's dictionary is not a sequence. It is a collection of items but each item (key:value pair) is not identified by positional index as in string, list or tuple.
# Hence, slicing operation cannot be done on a dictionary. Dictionary is a mutable object, so it is possible to perform add, modify or delete actions
# with corresponding functionality defined in dict class. These operations will be explained in a subsequent chapter.


## Python Set(집합) Data Type
# Set is a Python implementation of set as defined in Mathematics. A set in Python is a collection,
# but is not an indexed or ordered collection as string, list or tuple.
# An object cannot appear more than once in a set, whereas in List and Tuple, same object can appear more than once.
# Comma separated items in a set are put inside curly brackets or braces {}. Items in the set collection can be of different data types.
type({2023, "Python", 3.11, 5+6j, 1.23E-4})

# The position of items is optimized by Python to perform operations over set as defined in mathematics.
# A set can store only immutable objects such as number (int, float, complex or bool), string or tuple.
# If you try to put a list or a dictionary in the set collection, Python raises a TypeError.

# Hashing is a mechanism in computer science which enables quicker searching of objects in computer's memory. Only immutable objects are hashable.
# Even if a set doesn't allow mutable items, the set itself is mutable.
# Hence, add/delete/update operations are permitted on a set object, using the methods in built-in set class.
# Python also has a set of operators to perform set manipulation. The methods and operators are explained in latter chapters



## Python Boolean Data Types
# Python boolean type is one of built-in data types which represents one of the two values either True or False.
# Python bool() function allows you to evaluate the value of any expression and returns either True or False based on the expression.
a = True
# display the value of a
print(a)

# display the data type of a
print(type(a))

# Returns false as a is not equal to b
a = 2
b = 4
print(bool(a==b))

# Following also prints the same
print(a==b)

# Returns False as a is None
a = None
print(bool(a))

# Returns false as a is an empty sequence
a = ()
print(bool(a))

# Returns false as a is 0
a = 0.0
print(bool(a))

# Returns false as a is 10
a = 10
print(bool(a))




# -


