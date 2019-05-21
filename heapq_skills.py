import heapq

a = [4,2,1,3,5]
heap = heapq.heapify(a)

heapq.heappush(heap, 6)
x = heapq.heappop(heap)

# push item on the heap, then pop the smallest from the heap
x = heapq.heappushpop(heap, 7)

# pop the smallest from the heap, then push the new item
x = heapq.heapreplace(heap, 8)

# merge multiple sorted inputs into a single sorted output, return an iterator
b = [1,3,5,7]
c = [2,4,6,8]
it = heapq.merge(b, c)

# return a list of n largest elements from iterable
heapq.nlargest(3, it)

# return a list of n smallest elements from iterable
heapq.nsmallest(3, it)
