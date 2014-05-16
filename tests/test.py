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
