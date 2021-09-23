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
    """Returns True if k can be found by a dditionof any 2 numbers in list"""
    return True


## Classes
class Test_Solution(unittest.TestCase):

    # -Instance Methods
    def test_solution(self) -> None:
        self.assertTrue(solution(17, [10, 15, 3, 7]))


## Body
unittest.main()
