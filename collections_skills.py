# Counter: dict subclass for counting hashable objects
from collections import Counter

# we can use it like a dict
cnt = Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
	cnt[word] += 1
# which is the same as
cnt = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

import re
words = re.findall(r'\w+', open('hamlet.txt').read().lower())
Counter(words).most_common(10) # get top 10 frequent words

cnt.elements() # return elements according to count in arbitrary order
cnt.most_common(3) # return most common elements, n is optional

c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
c.subtract(d) # substract element from iterable or mapping
c.update(d) # update counter with iterable or mapping



# deque: list-like container with fast appends and pops on either end
from collections import deque

# create a deque
queue = deque(['a','b','c'], maxlen=10) # maxlen is optional to limit size of queue

# push
queue.append('d') # push from right side
queue.appendleft('d') # push from left side
queue.extend(['e', 'f'])
queue.extendleft(['e', 'f'])

# pop
queue.pop() # pop from right side
queue.popleft() # pop from left side

# most methods similar with list
queue.reverse()
queue.remove('c')
queue.count('c')
queue.clear()

# a special method
queue.rotate(3) # right shift 3 steps
queue.rotate(-3) # left shift 3 steps

# some useful recipes

# get the last n lines of a file
def tail(filename, n=10):
    return deque(open(filename), n)

# delete nth element from a queue, same as del queue[n]
def delete_nth(queue, n):
	queue.rotate(-n)
	queue.popleft()
	queue.rotate(n)

# calculate moving average with a sliding window
# moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
import itertools # also a useful tool
def moving_average(iterable, n=3):
    it = iter(iterable)
    d = deque(itertools.islice(it, n-1)) # get first n-1 slice to create a queue
    d.appendleft(0)
    s = sum(d)
    for elem in it:
        s += elem - d.popleft() # shift one step, remove first element, get new sum
        d.append(elem) # add new element
        yield s / float(n) # yield a new average



# defaultdict: dict subclass that calls a factory function to supply missing values
from collections import defaultdict

s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list) # for each key first encountered, an empty list [] has given to it.
for k, v in s:
	d[k].append(v)

# dict.setdefault() is slower than using a defaultdict directly
d = {}
for k, v in s:
    d.setdefault(k, []).append(v)

# design default value by myself
def constant_factory(value):
	# return a generator which always generates a fixed value
    return itertools.repeat(value).next

d = defaultdict(constant_factory('<missing>'))
d.update(name='John', action='ran')
print '%(name)s %(action)s to %(object)s' % d #'John ran to <missing>'



# OrderedDict: dict subclass that remembers the order entries were added
from collections import OrderedDict

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
OrderedDict(sorted(d.items(), key=lambda x: -x[1])) # usually work together with sorted()
OrderedDict(sorted(d.items(), key=lambda x: len(x[0])))

# OrderedDict remembers the order that keys were first inserted
d = OrderedDict()
d['a'] = 1
d['c'] = 3
d['b'] = 2
d # OrderedDict([('a', 1), ('c', 3), ('b', 2)])

# overwriting an existing entry, the original insertion position is left unchanged
d['a'] = 1
d # OrderedDict([('a', 1), ('c', 3), ('b', 2)])

# deleting an entry and reinserting it will move it to the end
val = d.pop('a') # pop value of 'a'
d['a'] = val # update the entry of 'a', will lead ('a',1) move to the end of dict
d # OrderedDict([('c', 3), ('b', 2), ('a', 1)])

# pop the item last inserted
d.popitem() # ('a', 1)
# pop the item first inserted
d.popitem(last=False) # ('c', 3)
