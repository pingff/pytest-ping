#!/usr/bin/python3

def evens(n):
    '''
    Returns a list of even numbers from 0 to n inclusive.
    '''
    return list(filter(lambda x: x % 2 == 0, range(0, n + 1)))
