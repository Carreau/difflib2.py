#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_difflib2
----------------------------------

Tests for `difflib2` module.
"""

import unittest

from difflib2 import difflib2
import difflib2.utils as utils
from difflib2.get_lcs_cut2 import get_lcs_cut2
from difflib2.low_m import low_m
from difflib2.low_ma import low_ma



def test_something(self):
    for case in utils.test_cases :
        for func in [get_lcs_cut2, low_m, low_ma]:
            func = get_lcs_cut2
            s1,s2,l = case
            r1 = func(s1,s2)
            assert(False)
            r2 = func(s2,s1)
            yield assert_sym, fun,s1,s2
            yield assert_correct, fun,s1,s2,l

def assert_sym(fun, s1,s2):
    assert(fun(s1,s2) == fun(s2,s1))

def assert_correct(fun, s1, s2 ,l):
    assert(fun(s1,s2)==l)

if __name__ == '__main__':
    unittest.main()
