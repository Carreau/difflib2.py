from __future__ import print_function
from array import array
from itertools import islice

def lcs_cut2(s1, s2, lcs_low_bound=0, bg=None, debug=False):
    """Compule the length of the LCS 2 sequences s1 and s2.
    
    lcs_low_bound : (int), hint of lower bound for the lenght of the lcs
    to search for. Default to 0.
    
    Algorithmic description:
    
    This is a derivation of Hirschberg's algorithm which include some
    optimisation for specific case.
    
    This shoudl use an O(n) memory (n = len(s1)) and should have a worse 
    case scenario time complexity of O(n**2). 
    
    In the best case scenario, (l ~ n) the time complexity is closer to O(n*l)
    where l is the lenght of the longest common subsequence. 
    Though, detail of implementaiton of s1 and s2 object slicing will 
    affect the optimal performace.
    
    bg is four debug purpose, to see how the algorithme behave visually
    using iptyhonblocks. uncomment bg lines below to use.
    """
    m = len(s1)
    n = len(s2) 
    if n==0 or m==0:
        return 0
    
    # rng is for row "rang" in french, "c" is for current and "p" for previous.
    # array are n+1 so that last elemnt is 0. This allow 
    # to avoid special casing j=0 as j-1 will wrap arround. 
    # alternative is to offset all indexes by 1, wichi becames hard to 
    # track
    rngc = array('i',[0 for x in range(n+1)]) ## current row
    rngp = array('i',[0 for x in range(n+1)]) ## previous row
    
    # current max value of the LCS durrgin the search.
    currentmax = lcs_low_bound
    
    # correspond to rngc[j-1], used to avoid lookup in the array
    # through the loop to shave off soem execution time.
    rngcjm = None
    
    # lower and upper bound for current loop on s2/j
    limm,limp = 0,n
    
    # lower bound for iteration on s1/i and 
    # another lower bound s2/j
    mini,minj = 0,0
    if debug:
        import pdb; pdb.set_trace()
    for i,c1 in enumerate(s1):

        # current row become previous, and we reuse previous to avoid
        # creating a new empty list.
        rngc, rngp = rngp, rngc

        minj=0
        limm = max(i-m+currentmax-1,0,minj-1)
        limp = min(i+n-currentmax+1,n)
        rngcjm = rngc[limm-1]
        if i < mini:
            print('skip i=',i)
            continue
        
        
        isl = islice(s2,limm,limp)
        rsl = range(limm,limp)
        zsl = zip(rsl,isl)
        for j,c2 in zsl:
#            if bg:
#                bg[i,j].green=255
            if c1 == c2 : 
                if i == 0 or j == 0:
                    newval = 1
                else:
                    newval = rngp[j-1]+1
                #   here we will peak ahead as far as possible
                # while the two string are matching, 
                # for strings with high similarity
                # this with give us hints on which part of the
                # lcs matrix we do not need to explore. 
                #
                #   we do this only once, if we are at 
                # the beginning of the matching streem. 
                if s1[i-1] != s2[j-1] or i==0 or j==0:
                    lookahead = 0 
                    k = min(m-i,n-j)
#                    print('looking ahead by',k,s1,s2, 'from',i,j, 'where current value is',newval)
#                    print('c1,c2 are',c1,c2)
                    for cx,cy in zip(s1[i+1:i+k],s2[j+1:j+k]):
#                        print('cx,cy are',cx,cy)
                        if cx==cy:
                            lookahead +=1
                        else:
                            break
#                    print('lookahead is', lookahead)
#                    if bg:
#                        for xx in range(0,lookahead):
#                            bg[i+xx,j+xx].blue=255
                    tmp = newval+lookahead
                    # if we are on i,j and have a value M
                    # then it is useless to process columns that have : 
                    # - a j value lower than M-j
                    # - a i value lower than M-i                            
#                    lminj=tmp-j
                    lminj=j+lookahead-tmp
                    lmini=i+lookahead -tmp
                    if lminj > minj:
                        minj=lminj
#                        for xx in range(0,minj):
#                            rngp[xx]=tmp-max(i+lookahead-tmp,j+lookahead-tmp)-1
#                            rngc[xx]=tmp-max(i+lookahead-tmp,j+lookahead-tmp)-1
#                    if bg:
#                        for xx in range(0,lminj):
#                            for lh in range(i,m):
#                                bg[lh,xx].red =255
#                        for xx in range(0,lmini):
#                            for lh in range(j,n):
#                                bg[xx,lh].red =255
#                        bg[i+lookahead,j+lookahead].red =255
                    if lmini > mini:
                        mini=lmini

                    if tmp > currentmax:
                        currentmax = tmp
                        limm,limp= max(i-m+currentmax,0,minj-1),min(i+n-currentmax+1,n)
                    if j >= limp+1:
                        break
                if newval > currentmax:
                    currentmax = newval
#                else :
#                    newval = currentmaxdd
            else :
                b = rngp[j]
                newval = rngcjm if rngcjm > b else b
            rngc[j] = rngcjm  = newval
    return rngc[-2]