import matplotlib.pyplot as plt
def report(df,dr, name='', guides =None):
    if not guides :
        guides = {}
    fig, (ax,ax2) = plt.subplots(ncols=2)
    fig.set_figwidth(fig.get_figwidth()*2)
    df.plot(x=df.index,ax=ax)
    mx= max(df.index)
    for k,v in guides.items():
        ax.plot(df.index,df.index**v/(mx**v)*df.ix[max(df.index)][k],'--',label='x**{}'.format(v))
    ax.get_ylim()

    #ax.plot(df.index,df.index/(mx)*df.ix[max(df.index)]['lcs_cut2'],'--')
    #ax.set_xlim(xmax=100)
    #ax.set_ylim(ymax=0.02)
    ax.set_xlabel('n,m length')
    ax.set_ylabel('time(s)')
    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_ylim(ymin=1e-5)
    #ax.vlines(50,*ax.get_ylim())

    dr.plot(x=dr.index,ax=ax2)
    ax2.set_xlabel('n,m length')
    ax2.set_ylabel('measured lcs length/real lcs length')
    #ax.set_yscale('log')
    ax2.set_xscale('log')
    ax2.set_ylim(ymax=1.1)
    ax2.set_ylim(ymin=-0.1)
    #ax2.vlines(50,*ax.get_ylim())
    ax2.set_title(name)

    pass

#report(df,dr)
