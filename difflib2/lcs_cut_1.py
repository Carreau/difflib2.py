@greg
def lcs_cut(s1, s2):
    m = len(s1)
    n = len(s2) 
    
    rngc = array('I',[0 for x in range(n)]) ## current row
    rngp = array('I',[0 for x in range(n)]) ## previous row
    currentmax = 0
    for i,c1 in enumerate(s1):
        rngc, rngp = rngp, rngc
        limm,limp= max(i-m+currentmax,0),min(i+n-currentmax+1,n)
        for j,c2 in zip(range(limm,limp),s2[limm:limp]):
            
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
        currentmax = max(currentmax,max(rngc))
    return rngc[-1]