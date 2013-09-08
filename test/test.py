# -*- coding: utf-8 -*-

import difflib2
import difflib2 as dl
import random

test_pairs = (
      ("Bonjour Monde",
       "Hello World")
      ,("a"*50,
       "a"*50),
      ("a"*25+"b"+"a"*25,
       "a"*51)
      ,("abcdeghjkl",
       "acefghijkl")
      ,("abc-efghijkl",
       "abcdefgh-jkl")
      ,("0123456789",
       "012345789")
      ,(u"ceci est une première chaine de caractere test pour voir es différences",
        u"ceci est le complementaire de la première chaine de caractère test pour aussi voir les différence")
      )



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

def test_slicify():
    s = []
    s0 = []
    for i in range(5):
        k,l = random.randint(0,20),random.randint(1,10)
        s0.append((k,k+l-1))
        s.extend(range(k,k+l))

    a = dl.groupper(s)
    b = list(dl.itergroup(s))
    assert a == b

    cmp = []
    for start,stop in b:
        cmp.extend(range(start,stop+1))
    
    assert s==cmp
