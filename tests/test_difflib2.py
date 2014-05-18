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


class TestDifflib2(unittest.TestCase):

    def setUp(self):
        pass

    def test_something(self):
        for case in utils.test_cases :
            s1,s2,l = case
            r1 = func(s1,s2)
            r2 = func(s2,s1)
            assert(r1 == l)
            assert(r2 == l)
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()
