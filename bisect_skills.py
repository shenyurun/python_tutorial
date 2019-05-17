# bisect:  maintaining a list in sorted order
import bisect

# search the insertion point for x in a to maintain sorted order
# search time complexity: O(logN)
bisect.bisect_left(a, x)	# returns the leftmost index to insert x in a
bisect.bisect_right(a, x)	# returns the rightmost index to insert x in a
bisect.bisect(a, x)			# same as bisect_right

# insert x into a by the insertion point
# insert time complexity: O(N), since insertion is bottleneck!
# so it's quite expensive to use bisect successively
# often use it on a pre-computed list
bisect.insort_left(a, x)	# insert x into a at the leftmost index
bisect.insort_right(a, x)	# insert x into a at the rightmost index
bisect.insort(a, x)			# same as insort_right


# some recipes
# useful for numeric table lookups
def grade(score, breakpoints=[60, 70, 80, 90], grades='FDCBA'):
    i = bisect(breakpoints, score)
    return grades[i]

[grade(score) for score in [33, 99, 77, 70, 89, 90, 100]]
