__author__ = 'nikoladang'

def solution(A, K):
    if A:
        for i in range(K):
            lastElement = A.pop()
            A.insert(0, lastElement)
    return A

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert solution([3, 8, 9, 7, 6], 3) == [9, 7, 6, 3, 8]
    assert solution([], 3) == []



