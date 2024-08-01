#!/usr/bin/env python3
'''alx task 9's module .py
'''
from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''this enters the length of a list of sequences...
    '''
    return [(i, len(i)) for i in lst]
