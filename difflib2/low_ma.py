from .utils import greg
from array import array

@greg
def lcs_low_ma(s1, s2):
    """Low memory implementation using array"""
    
    
    m = len(s1)
    n = len(s2) 
    
    rngc = array('I',[0 for x in range(n)]) ## current row
    rngp = array('I',[0 for x in range(n)]) ## previous row
    
    for i,c1 in enumerate(s1):
        rngc, rngp = rngp, rngc
        for j,c2 in enumerate(s2): 
            if c1 == c2 : 
                if i == 0 or j == 0:
                    rngc[j] = 1
                else:
                    rngc[j] = rngp[j-1]+1
            else :
                if j == 0:
                    rngc[0] = rngp[0]
                elif i == 0: 
                    rngc[j] = rngc[j-1]
                else :
                    rngc[j] = max(rngc[j-1],rngp[j])
    return rngc[-1]
