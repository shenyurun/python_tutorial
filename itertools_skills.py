# itertools: a number of iterator building blocks
# more details: https://docs.python.org/2/library/itertools.html#itertools.islice
from itertools import *

# infinite iterators

# count(): make an iterator that returns evenly spaced values starting with n
# often used as an argument to imap() to generate consecutive data points
# also used with izip() to add sequence numbers
gen1 = count(10)
gen2 = count(2.5, 0.5)
gen3 = izip(count(1), ['a', 'b', 'c'])

# cycle(): make an iterator returning elements from the iterable and saving a copy of each
# when the iterable is exhausted, return elements from the saved copy, repeating indefinitely
cycle(['a','b','c'])

# repeat(): make an iterator that returns object over and over again
# runs indefinitely unless the times argument is specified
# used as argument to imap() for invariant function parameters
# also used with izip() to create constant fields in a tuple record
gen1 = repeat('over-and-over')
gen2 = repeat('over-and-over', 5):



# iterators terminating on the shortest input sequence
# chain(): make an iterator that returns elements from the first iterable until it is exhausted,
# then proceeds to the next iterable, until all of the iterables are exhausted
# used for treating consecutive sequences as a single sequence
gen1 = chain([1, 2, 3], ['a', 'b', 'c'])



# return r length subsequences of elements from the input iterable
itertools.combinations('abcd', 2)

# return r length subsequences of elements from the input iterable
# allowing individual elements to be repeated more than once
itertools.combinations_with_replacement('abcd', 2)

