'''string'''
str1 = 'Say hi to Bob\'s mother.'
str1 = "Say hi to Bob's mother."

str1.capticalize()
str1.title()

str1.lower()
str1.upper()
str1.islower()
str1.isupper()

str1.find(str2) #return -1 if not found
str1.index(str2) #throw exception if not found

str1.replace(' ', '-')

str1.startswith(str2)
str1.endswith(str2)

str1.center(20, '*')
str1.rjust(20, '*')
str1.ljust(20, '*')
'1234'.zfill(20)

str1[2:]
str1[2:4]
str1[2::2]
str1[::2]
str1[::-1] #reverse
str1[-3:-1] #index from end

str1.isalpha()
str1.isalnum()
str1.isspace()
str1.istitle()
str1.isdigit() # Unicode数字，全角数字（双字节），byte数字（单字节），罗马数字
str1.isnumeric() # Unicode数字，全角数字（双字节），罗马数字，汉字数字
str1.isdecimal() # Unicode数字，全角数字（双字节）

str1.strip()
str1.lstrip()
str1.rstrip()

' '.join(['My', 'name', 'is', 'Simon'])
'My name is Simon'.split()
'My name is Simon'.rsplit(' ', 2)

'''list'''
list1 = ['abc'] * 10

list1.append('abc')
list1.insert(idx, 'abc')

list1 += ['ab', 'cd']
list1.extend(['ab', 'cd'])

list1.remove('abc') # remove the first matching value
del list1[idx] # remove by a specific index
list1.pop(idx) # remove by a specific index and return the value

list1.clear()

list2 = list1 # direct to same list
list2 = list1[:] # copy a new list

list2 = sorted(list1) # list1 is not changed
list2 = sorted(list1, reverse=True)
list2 = sorted(list1, key=len)
list1.sort(reverse=True) # list1 is changed

list1 = [x for x in range(10)]
list1 = [x+y for x in 'abcd' for y in '123'] #return a list of all combinations of 'abcd' and '123'

list1 = [x**2 for x in range(1000)] # a list
func1 = (x**2 for x in range(1000)) # a generator
print(sys.getsizeof(list1))
print(sys.getsizeof(func1))

# fibonacci example using generator
def fib(n):
	a, b = 0, 1
	for _ in range(n):
		a, b = b, a+b
		yield a

for val in fib(10):
	print val


# transpose a matrix
matrix = [
	[1,2,3],
	[4,5,6],
]
zip(*matrix)

# more about unpacking
args = [3, 6]
range(*args)

def func(a=0, b=1, c=2): return a+b+c
d = {'a':10, 'b':20, 'c':30}
func(**d)


'''tuple'''
tup1 = ('abc', 123, True)
# same indexing and slicing grammar as string and list
# cannot modify elements
# can transform from and to a list
list1 = list(tup1)
tup1 = tuple(list1)
# tuple is more safe and conivient to be shared by multiple threads
# tuple saves more time and space compared with list


'''set'''
set1 = {1,2,3,2,3}
set1 = set(range(10))
set1 = set(list1)
set1 = set(tup1)

set1.add(4)
set1.update([4,5,6])

set1.discard(4) # remove val from set, will not raise keyerror if val not in set
set1.remove(4) # remove val from set, will raise keyerror if val not in set
set1.pop() # remove an arbitrary val from set, will raise keyerror if set is empty

set1.clear()

# intersection
set3 = set1 & set2
set1.intersection(set2)
# symmetric difference
set3 = set1 ^ set2
set1.symmetric_difference(set2)
# union
set3 = set1 | set2
set1.union(set2)
# difference
set3 = set1 - set2
set1.difference(set2)

# is subset
print set1 <= set2
print set1.issubset(set2)
# is superset
print set1 >= set2
print set1.issuperset(set2)


'''dict'''
dict1 = {'a':0, 'b':1, 'c':2}
dict1['d'] = 4
dict1.update(a=10, e=20)
dict1.update({'a':10, 'e':20})

dict1['a']
dict1.get('a')
dict1.get('x', -1)

dict1.popitem() # remove an arbitrary (key, value) pair from dict
dict1.pop('a') # remove given key, and return corresponding value, throw keyerror if key doesn't exist
dict1.pop('a', -1) # remove given key, and return corresponding value, return default value if key doesn't exist
del dict1['a'] # remove given key, and return corresponding value, throw keyerror if key doesn't exist

dict1.clear()


et1.clear()

# intersection
set3 = set1 & set2
set1.intersection(set2)
# symmetric difference
set3 = set1 ^ set2
set1.symmetric_difference(set2)
# union
set3 = set1 | set2
set1.union(set2)
# difference
set3 = set1 - set2
set1.difference(set2)

# is subset
print set1 <= set2
print set1.issubset(set2)
# is superset
print set1 >= set2
print set1.issuperset(set2)


'''dict'''
dict1 = {'a':0, 'b':1, 'c':2}
dict1['d'] = 4
dict1.update(a=10, e=20)
dict1.update({'a':10, 'e':20})

dict1['a']
dict1.get('a')
dict1.get('x', -1)
dict1.setdefault('a', 10) # if key exists, return value, if not exists, add (key, value) pair and return the default value

dict1.popitem() # remove an arbitrary (key, value) pair from dict
dict1.pop('a') # remove given key, and return corresponding value, throw keyerror if key doesn't exist
dict1.pop('a', -1) # remove given key, and return corresponding value, return default value if key doesn't exist
del dict1['a'] # remove given key, and return corresponding value, throw keyerror if key doesn't exist

dict1.clear()


# built-in functions

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

