import difflib2
import difflib2 as dl
import random



def test1():
    assert difflib2.lcs('foo','foo') == 'foo'

def testempty():
    assert difflib2.lcs('','') == ''

def testempty2():
    assert difflib2.lcs_len('','') == 0

def test_empy_matrix():
    assert dl.lcs_matrix('','') == []

def test_equal_len():
    for i in range(10):
        s1 = [random.randint(0,10) for i in range(random.randint(40,50))]
        s2 = [random.randint(0,10) for i in range(random.randint(40,50))]
        ss = (s1,s2)
        assert dl.lcs_len(s1,s2) == dl.lcs_matrix(s1,s2)[-1][-1]
        both = dl.lcs_low_m_anlcs(s1,s2)
        assert both.length == dl.lcs_len(*ss)
        assert both.length == len(both.lcs)

from difflib2 import difflib2
import difflib2.utils as utils
from difflib2.get_lcs_cut2 import get_lcs_cut2
from difflib2.low_m import lcs_low_m
from difflib2.low_ma import lcs_low_ma



def test_something():
    for case in utils.test_cases :
        for func in [get_lcs_cut2, lcs_low_m, lcs_low_ma]:
            func = get_lcs_cut2
            s1,s2,l = case
            r1 = func(s1,s2)
            r2 = func(s2,s1)
            yield assert_sym, func,s1,s2
            yield assert_correct, func,s1,s2,l

def assert_sym(fun, s1,s2):
    assert(fun(s1,s2) == fun(s2,s1))

def assert_correct(fun, s1, s2 ,l):
    assert(fun(s1,s2)==l)
