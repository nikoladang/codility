__author__ = 'nikoladang'

# http://stackoverflow.com/questions/873327/pythons-most-efficient-way-to-choose-longest-string-in-list
# http://stackoverflow.com/questions/627435/how-to-remove-an-element-from-a-list-by-index-in-python

def solution(N):
    b = bin(N)[2:]
    alist = b.split("1")
    del(alist[-1]) # remove trailing zeros from list
    longestItem = max(alist, key=len)
    return len(longestItem)

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert solution(9) == 2
    assert solution(1041) == 5
    assert solution(16) == 0
    assert solution(1024) == 0
    assert solution(51712) == 2
    assert solution(20) == 1


