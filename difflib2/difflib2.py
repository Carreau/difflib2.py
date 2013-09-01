# coding : utf-8

"""
difflib2 : a surpriseless difflib for developper.

difflib does not attempt to be smart, or to assume
what you will diff is either source-code or string. 


"""


def lcsmatrix(s1, s2):
    """ Compute the lcs matrix for s1 vs s2

    s1 : sequence (of len m)
    s2 : sequence (of len n)

    return lcs_matrix[1:n][1:m] (list of list)

    This is not the fastest, nor the more memory efficient
    way to compute a lcs in many cases. It is a quadratic algorithm
    both in time and memory.

    lcs_matrix is returned without the 0-padded row.

    >>> lcsmatrix('abc','bacd')
    [[0, 1, 0, 0],
     [1, 1, 1, 1],
     [1, 1, 2, 2]]

    """
    m = len(s1)
    n = len(s2) 
    mtx = [[0 for x in range(n)] for y in range(m)]

    for i,c1 in enumerate(s1):
        for j,c2 in enumerate(s2): 
            if c1 == c2 : 
                if i == 0 or j == 0:
                    mtx[i][j] = 1
                else:
                    mtx[i][j] = mtx[i-1][j-1]+1
            else :
                if i == 0: 
                    mtx[i][j] = 0
                elif j == 0:
                    mtx[i][j] = mtx[i-1][j]
                else :
                    mtx[i][j] = max(mtx[i][j-1],mtx[i-1][j])
    return mtx


def lcs_low_m(s1, s2):
    """ return len of the lcs of s1 and  s2
    
    s1 : sequence , (len = n)
    s2 : sequence , (len = m)

    Try to be memory efficient O(n)
    CPU time O(m.n)

    Usually faster than computing the full lcs matrix.
    And generaly best algorythm to use if you are only interested
    in the edit distance, and are working with relatively short sequences, 
    without knowing specific property of your alphabet...
    """
    
    m = len(s1)
    n = len(s2) 
    
    # one can be smarter by storing only n+1 element
    # but the hevy use of modulo slow thig down a lot.

    rngc = [0 for x in range(n)] ## current row
    rngp = [0 for x in range(n)] ## previous row
    
    for i,c1 in enumerate(s1):
        rngc, rngp = rngp, rngc
        for j,c2 in enumerate(s2): 
            if c1 == c2 : 
                if i == 0 or j == 0:
                    rngc[j] = 1
                else:
                    rngc[j] = rngp[j-1]+1
            else :
                if i == 0: 
                    rngc[j] = 0
                elif j == 0:
                    rngc[j] = rngp[j]
                else :
                    rngc[j] = max(rngc[j-1],rngp[j])
    return rngc[-1]




def backtrack(C, X, Y):
    """ backtrack a lcs matrix to get one of the LCS

    C : lcs matrix
    X : sequence 1
    Y : sequence 2
    
    Again, not the more efficient if you are interested in the lcs. 
    """
    return _backtrack(C, X, Y)

def _backtrack(C, X, Y,  ii=None, jj=None):
    """
       cf :meth:backtrack docstring for more info

       ii,jj : backtrack index, used internally to be called recursively.

    """
    if ii==None and jj==None :
        ii = len(X)-1
        jj = len(Y)-1
    if ii == -1 or jj == -1:
        return []
    elif X[ii] == Y[jj]:
        p = _backtrack(C ,X, Y, ii-1, jj-1)
        p.append((ii,jj))
        return p
    else:
        if C[ii][jj-1] > C[ii-1][jj]:
            return _backtrack(C, X, Y, ii, jj-1)
        else:
            return _backtrack(C, X, Y, ii-1, jj)

def lcs(s1, s2):
    """
    return the longuest common subsequence of the 2 sequences.
    
    if both are string return the lcs as a string
    if both are unicode return the lcs as unicode
    
    Otherwise, return the lcs as a list.
    """
    arestring = (type(s1) is str) and (type(s2) is str)
    areunicode = (type(s1) is unicode) and (type(s2) is unicode)
    
    C = lcsmatrix(s1,s2)
    ig = backtrack(C, s1, s2)
    i1, i2 = zip(*ig)
    
    lcs = [s1[i] for i in i1]
    
    if areunicode :
       return  u''.join(lcs)
    if arestring:
        return ''.join(lcs)
    return lcs
