#!/usr/bin/python
##-------------------------------##
## Daily Coding Problem          ##
## Written By: Ryan Smith        ##
##-------------------------------##
## Day 01                        ##
##-------------------------------##

## Imports
import unittest


## Functions
def solution(k: int, list_: list[int]) -> bool:
    """
    O(n^2)
    Returns True if k can be found by addition of any 2 numbers in list
    """
    for a, c in enumerate(list_):
        for b, d in enumerate(list_):
            if a == b:
                continue
            if c + d == k:
                return True
    return False


## Classes
class Sum_of_Numbers(unittest.TestCase):

    # -Instance Methods
    def test_solution(self) -> None:
        self.assertTrue(solution(17, [10, 15, 3, 7]))
        self.assertTrue(solution(5, [1, 2, 4, 8]))
        self.assertTrue(solution(2, [1, 1, 2, 3]))
        self.assertFalse(solution(10, [5, 6, 8, 9]))
        self.assertFalse(solution(9, [1, 5, 6]))
        self.assertFalse(solution(5, [10, 15, 3, 7]))


## Body
unittest.main()
