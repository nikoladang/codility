__author__ = 'nikoladang'
# http://stackoverflow.com/questions/1267869/how-can-i-force-division-to-be-floating-point-in-python

from __future__ import division

import math

def solution(X, Y, D):
    # write your code in Python 2.7
    x = int(math.ceil((Y-X)/D))
    return x


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert solution(10, 85, 30) == 3
