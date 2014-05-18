fn = None
def test_case(case, r=3, nt=3, agree=True, ldict=None):
    global gdict
    if not ldict:
        ldict = gdict
    if len(case) == 4:
        s1,s2,l,name = case
    else :
        s1,s2,l = case
        name = '...'
    df = pd.DataFrame()
    global dl
    dl = pd.DataFrame()
    # warmup
#    %timeit -o -r{r} -n{nt} -q lcsmatrix(s1,s2)
    for func in gdict.values():
        # the way timeit work, we need to use a global
        global fn 
        fn = func
        #print('testing', fn.__name__)
        dl[func.__name__] = [fn(s1,s2)]
        u  = %timeit -o -r{r} -n{nt} -q fn(s1,s2)
#        u  = %timeit -o fn(s1,s2)
        df[func.__name__] = u.all_runs


    # lcs_low_m(s1,s2)

    fig, (ax,ax2) = plt.subplots(ncols=2)
    fig.set_figwidth(2*fig.get_figwidth())
    df.boxplot(ax=ax)
    ax.set_ylabel('time (s), lower is better')
    try:
        ax.set_title(name+' lenght:%d,%d' % (len(s1),len(s2)))
    except:
        pass
    # are the results the same ?


    dl.boxplot(ax=ax2)
    ax2.set_ylabel('calculated LCS length')
    pass