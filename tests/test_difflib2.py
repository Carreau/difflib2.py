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
            assert()
        pass

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()