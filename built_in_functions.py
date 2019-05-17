# built-in functions
# details: https://docs.python.org/2.7/library/functions.html

# filter(func, seq): return a seq of items(list, tuple, string...) from the input seq for which func(item) is true
def f(x): return x.isdigit()
filter(f, ['12','ab','3f'])

# map(func, seq): return the seq of func(item) for each item in input seq
def f(x): return x**2
map(f, [1,2,3])

def add(x,y): return x+y
map(add, [1,2,3], [4,5,6])

# reduce(func, seq): return a single value constructed by calling func(with two params) on the first two items of the sequence
# then on the result and the next item, and so on.
reduce(add, range(1,11)) # return sum of [1,2,...,10]


# math functions
abs()
sum()
min()
max()
pow()
divmod()	# Returns a Tuple of Quotient and Remainder
hash()	# returns hash value of an object
round()		# rounds a floating point number to ndigits places
'''
Important!!!
	Python 2.7:
		values are rounded to the closest multiple of 10 to the power minus ndigits
		if two multiples are equally close, rounding is done away from 0
		so round(0.5) == 1, round(-0.5) == -1
	Python 3.5:
		values are rounded to the closest multiple of 10 to the power minus ndigits
		if two multiples are equally close, rounding is done toward the even choice
		so round(0.5) == 0, round(-0.5) == 0
'''


# type conversion
int()
float()
complex(a, b) # returns a complex number: a+bj
str()
bool()
bin()	# converts integer to binary string
hex()	# converts integer to hexadecimal
oct()	# converts integer to octal
bytes()	# converts object to immutable bytes object
chr()	# Returns a Character (a string) from an Integer
ord()	# returns Unicode code point for Unicode character


# generate list, dict, tuple, or other objects
list()
dict()
tuple()
set()
frozenset() # frozenset is immutable set
bytearray()	# returns array of given byte size
object()	# Creates a Featureless Object

# boolean functions
all()	# returns true when all elements in iterable is true
any()	# Checks if any Element of an Iterable is True

# sth for re-ordering
sorted()	# returns sorted list from a given iterable
reversed()	# returns reversed iterator of a sequence

# sth for iteration
iter()		# returns iterator for an object
next()		# Retrieves Next Element from Iterator
enumerate()	# Returns an Enumerate Object
range()		# return sequence of integers between start and stop
slice()		# creates a slice object specified by range(), like range(slice(0,10,2))
zip()		# Returns an Iterator of Tuples

# sth about formatting
format()	# returns formatted representation of a value
input()		# reads and returns a line of string
repr()		# returns printable representation of an object

# sth for class attributes and methods
getattr()		# returns value of named attribute of an object
hasattr()		# returns whether object has named attribute
setattr()		# sets value of an attribute of object
delattr()		# deletes attribute From the object
dir()			# list all attributes of object
property()		# returns a property attribute
callable()		# Checks if the Object is Callable
classmethod()	# returns class method for given function
staticmethod()	# creates static method from a function
isinstance()	# Checks if a Object is an Instance of Class
issubclass()	# Checks if a Object is Subclass of a Class
super()			# Allow you to Refer Parent Class by super
vars()			# Returns __dict__ attribute of a class

# sth never used before
globals()		# returns dictionary of current global symbol table
locals()		# Returns dictionary of a current local symbol table
id()			# Returns Identify of an Object
memoryview()	# returns memory view of an argument
compile()		# Returns a Python code object
eval()			# Runs Python Code Within Program
exec()			# Executes Dynamically Created Program
