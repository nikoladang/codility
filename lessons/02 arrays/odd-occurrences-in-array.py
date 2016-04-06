__author__ = 'nikoladang'
# http://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
# http://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item-in-python
# *[solved] performance test fail --> http://www.martinkysel.com/codility-oddoccurrencesinarray-solution/

def solution1(A):
    a = set(A)
    for item in a:
        if (A.count(item) % 2) == 1:
            return item


def solution(A):
    unpairValue = 0
    for value in A:
        unpairValue ^= value
    return unpairValue


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert solution([9, 3, 9, 3, 9, 7, 9]) == 7
