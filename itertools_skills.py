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

# compress(): make an iterator that filters elements from data returning only those 
# that have a corresponding element in selectors that evaluates to True
# stops when either the data or selectors iterables has been exhausted
gen1 = compress('ABCDEF', [1,0,1,0,1,1])

# dropwhile(): make an iterator that drops elements from iterable until the predicate is true
# afterwards, returns every element left
# the iterator does not produce any output until the predicate first becomes false
gen1 = dropwhile(lambda x: x<5, [1,4,6,4,1])

# takewhile(): make an iterator that returns elements from iterable until the predicate is false
gen1 = takewhile(lambda x: x<5, [1,4,6,4,1])

# ifilter(): make an iterator that filters elements from iterable, 
# returning only those for which the predicate is true
gen1 = ifilter(lambda x: x<5, [1,4,6,4,1])

# ifilterfalse(): make an iterator that filters elements from iterable,
# returning only those for which the predicate is false
# if predicate is None, return the items that are false
gen1 = ifilterfalse(lambda x: x<5, [1,4,6,4,1])

# groupby(): make an iterator that returns consecutive keys and groups from the iterable
# key is a function computing a key value for each element
# if not specified or is None, key defaults to an identity function and returns the element unchanged
# generally, the iterable needs to already be sorted on the same key function
a = ['aa', 'ab', 'abc', 'bcd', 'abcde']
for i, k in groupby(a, len):
	print i, list(k)

# groupby() returns iteratable, save it to list if needed
groups = []
uniquekeys = []
data = sorted(data, key=keyfunc)
for k, g in groupby(data, keyfunc):
    groups.append(list(g))      # store group iterator as a list if needed
    uniquekeys.append(k)		# store group key if needed

# another example group by key value
from operator import itemgetter
d = dict(a=1, b=2, c=1, d=2, e=1, f=2, g=3)
di = sorted(d.iteritems(), key=itemgetter(1))
for k, g in groupby(di, key=itemgetter(1)):
    print k, map(itemgetter(0), g)

# islice(): make an iterator that returns selected elements from the iterable
gen1 = islice('ABCDEFG', 2) 			# --> A B
gen2 = islice('ABCDEFG', 2, 4)			# --> C D
gen3 = islice('ABCDEFG', 2, None)		# --> C D E F G
gen4 = islice('ABCDEFG', 0, None, 2)	# --> A C E G
gen5 = islice(count(), 0, 100, 10)

# imap(): make an iterator that computes the function using arguments from each of the iterables
gen1 = imap(pow, (2,3,10), (5,2,3))
gen2 = imap(lambda x,y: (x, y, x*y), xrange(5), xrange(5,10))

# starmap(): make an iterator that computes the function using arguments obtained from the iterable
# argument parameters are already grouped in tuples from a single iterable
gen1 = starmap(pow, [(2,5), (3,2), (10,3)])

# tee(): return n independent iterators copy from a single iterable
r = islice(count(), 5)
gen1, gen2, gen3 = tee(r, 3)

# izip(): make an iterator that aggregates elements from each of the iterables
# iteration stops if any of the iterable is exhausted
gen1 = izip('ABCD', 'xy') # --> Ax By

# izip_longest(): 
# if the iterables are of uneven length, missing values are filled-in with fillvalue
# iteration continues until the longest iterable is exhausted
gen1 = izip_longest('ABCD', 'xy', fillvalue='-') # --> Ax By C- D-

# permutations():

# combinatoric generators

# product(): return Cartesian product of input iterables
product('ABCD', 'xy')		# --> Ax Ay Bx By Cx Cy Dx Dy
product(range(2), repeat=3)	# --> 000 001 010 011 100 101 110 111

# permutations(): return successive r length permutations of elements in the iterable
# if r is not specified or is None, then r defaults to the length of the iterable
# and all possible full-length permutations are generated
permutations('ABCD', 2)		# --> AB AC AD BA BC BD CA CB CD DA DB DC
permutations(range(3))		# --> 012 021 102 120 201 210

# combinations(): return r length subsequences of elements from the input iterable
# combinations are emitted in lexicographic sort order
# so if the input iterable is sorted, the combination tuples will be sorted too
combinations('ABCD', 2)		# --> AB AC AD BC BD CD
combinations(range(4), 3) 	# --> 012 013 023 123

# combinations_with_replacement(): return r length subsequences of elements from the input iterable
# allowing individual elements to be repeated more than once
combinations_with_replacement('ABC', 2)	# --> AA AB AC BB BC CC
# elements are treated as unique based on their position, not on their value
# so there will be repeated elements if interable contains repeated values
combinations_with_replacement('BBC', 2)	# --> BB BB BC BB BC CC



# some recipes, some of them is worth taken

def take(n, iterable):
    "Return first n items of the iterable as a list"
    return list(islice(iterable, n))

def tabulate(function, start=0):
    "Return function(0), function(1), ..."
    return imap(function, count(start))

def consume(iterator, n=None):
    "Advance the iterator n-steps ahead. If n is None, consume entirely."
    # Use functions that consume iterators at C speed.
    if n is None:
        # feed the entire iterator into a zero-length deque
        collections.deque(iterator, maxlen=0)
    else:
        # advance to the empty slice starting at position n
        next(islice(iterator, n, n), None)

def nth(iterable, n, default=None):
    "Returns the nth item or a default value"
    return next(islice(iterable, n, None), default)

def all_equal(iterable):
    "Returns True if all the elements are equal to each other"
    g = groupby(iterable)
    return next(g, True) and not next(g, False)

def quantify(iterable, pred=bool):
    "Count how many times the predicate is true"
    return sum(imap(pred, iterable))

def padnone(iterable):
    """Returns the sequence elements and then returns None indefinitely.

    Useful for emulating the behavior of the built-in map() function.
    """
    return chain(iterable, repeat(None))

def ncycles(iterable, n):
    "Returns the sequence elements n times"
    return chain.from_iterable(repeat(tuple(iterable), n))

def dotproduct(vec1, vec2):
    return sum(imap(operator.mul, vec1, vec2))

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)

def repeatfunc(func, times=None, *args):
    """Repeat calls to func with specified arguments.

    Example:  repeatfunc(random.random)
    """
    if times is None:
        return starmap(func, repeat(args))
    return starmap(func, repeat(args, times))

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper('ABCDEFG', 3, 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def roundrobin(*iterables):
    "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
    # Recipe credited to George Sakkis
    pending = len(iterables)
    nexts = cycle(iter(it).next for it in iterables)
    while pending:
        try:
            for next in nexts:
                yield next()
        except StopIteration:
            pending -= 1
            nexts = cycle(islice(nexts, pending))

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def unique_everseen(iterable, key=None):
    "List unique elements, preserving order. Remember all elements ever seen."
    # unique_everseen('AAAABBBCCDAABBB') --> A B C D
    # unique_everseen('ABBCcAD', str.lower) --> A B C D
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in ifilterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen_add(k)
                yield element

def unique_justseen(iterable, key=None):
    "List unique elements, preserving order. Remember only the element just seen."
    # unique_justseen('AAAABBBCCDAABBB') --> A B C D A B
    # unique_justseen('ABBCcAD', str.lower) --> A B C A D
    return imap(next, imap(itemgetter(1), groupby(iterable, key)))

def iter_except(func, exception, first=None):
    """ Call a function repeatedly until an exception is raised.

    Converts a call-until-exception interface to an iterator interface.
    Like __builtin__.iter(func, sentinel) but uses an exception instead
    of a sentinel to end the loop.

    Examples:
        bsddbiter = iter_except(db.next, bsddb.error, db.first)
        heapiter = iter_except(functools.partial(heappop, h), IndexError)
        dictiter = iter_except(d.popitem, KeyError)
        dequeiter = iter_except(d.popleft, IndexError)
        queueiter = iter_except(q.get_nowait, Queue.Empty)
        setiter = iter_except(s.pop, KeyError)

    """
    try:
        if first is not None:
            yield first()
        while 1:
            yield func()
    except exception:
        pass

def random_product(*args, **kwds):
    "Random selection from itertools.product(*args, **kwds)"
    pools = map(tuple, args) * kwds.get('repeat', 1)
    return tuple(random.choice(pool) for pool in pools)

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(xrange(n), r))
    return tuple(pool[i] for i in indices)

def random_combination_with_replacement(iterable, r):
    "Random selection from itertools.combinations_with_replacement(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.randrange(n) for i in xrange(r))
    return tuple(pool[i] for i in indices)

def tee_lookahead(t, i):
    """Inspect the i-th upcomping value from a tee object
       while leaving the tee object at its current position.

       Raise an IndexError if the underlying iterator doesn't
       have enough values.

    """
    for value in islice(t.__copy__(), i, None):
        return value
    raise IndexError(i)