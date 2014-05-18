from __future__ import print_function
from array import array

def lcs_cut2(s1, s2, bg=None):    
    m = len(s1)
    n = len(s2) 
    rngc = array('I',[0 for x in range(n)]) ## current row
    rngp = array('I',[0 for x in range(n)]) ## previous row
    currentmax = 0
    for i,c1 in enumerate(s1):
        rngc, rngp = rngp, rngc
        limm,limp= max(i-m+currentmax,0),min(i+m-currentmax,m)
        #print(limm,limp) 
        for j,c2 in zip(range(limm,limp),s2[limm:limp]):
            if j > limp:
                #limp can be updated
                break
            if c1 == c2 : 
                if i == 0 or j == 0:
                    newval = 1
                else:
                    newval = rngp[j-1]+1
                    if s1[i-1] !=  s2[j-1]:
                        lookahead = -1
                        k = min(m-i,n-j)
#                        if bg :
#                            for ii,jj in zip(range(i,i+k),range(j,j+k)):
#                                bg[ii,jj].blue = 255
                        for cx,cy in zip(s1[i:i+k],s2[j:j+k]):
                            if cx==cy:
                                lookahead +=1
                            else:
                                break
                        tmp = rngc[j]+lookahead 
                        if tmp > currentmax:
                            currentmax = tmp
                            limp= min(i+m-currentmax,m)
                rngc[j] = newval
                if newval > currentmax:
                    currentmax = newval
            else :
                if j == 0:
                    rngc[0] = rngp[0]
                #elif i == 0: 
                #    rngc[j] = rngc[j-1]
                else :
                    a = rngc[j-1]
                    b = rngp[j]
                    rngc[j] = a if a > b else b
#                   rngc[j] = max(rngc[j-1],rngp[j])

    return rngc[-1]