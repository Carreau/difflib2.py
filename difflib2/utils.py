"""

test_case :

    a few test cases to try with LCS implementation, it is a list of 3-tuple
    for which the 2 first element are sequence to compare, and the last element
    the length of the LCS. 

"""


test_cases=[
    ('+'+'fgh+jklmnop','-'+'fghijklmnop', 10),
    ('+'+'fgh+jklmnop'*2,'-'+'fghijklmnop'*2, 20),
    ('ddb','ded',2),
    ('abcdef','abcdef',6),
    ('abcde','abcde',5),
    (list(range(10)),list(range(10)),10),
    ('ab','ab',2),
    ('abx','ab',2),
    ('axb','ab',2),
    ('abx','aby',2),
    ('axb','aby',2),
    ('lmnopfghjklm','lmnopfghjklmn',12),
    ('abcdEfghijklmnopqrSSStuvwxyz1234567890','abcdefghijKLLmnopqrstuvwxyz1234567890',32),
    ('xxxxxxx and something that matches',' and something that matchesyyyyyyy',27)
]


class SymetryError(Exception):
    pass

gdict = {}

def greg(function):
    """Globar REGistration of function aka "greg"
    """
    gdict[function.__name__] = function
    for s1,s2,l in test_cases:
        s1s2 = function(s1,s2)
        if s1s2 != l:
            raise ValueError('not correct', s1s2,s1,s2, l)

        s2s1 = function(s2,s1)
        
        if s1s2 != s2s1: 
            raise SymetryError('not symetric',s1s2 ,s2s1,l)

    print('this implementation passes basic tests')
    return function

def opt_common_char(func):
    def closure(s1,s2,*args,**kwargs):
        s = set(s1).intersection(set(s2))
        s11 = [c for c in s1 if c in s]
        s22 = [c for c in s2 if c in s]
#        print('will pass ',s11, s22, 'instead of ', s1, s2)
        return func(s11,s22,*args, **kwargs)
    closure._wrapped = func
    return closure
        
def rem_common_extrem(func):
    def closure(s1,s2,*args,**kwargs):
        delta = 0 
        ss1 = list(s1)
        ss2 = list(s2)
        rem = []
        for k in range(2):
            ss1 = list(reversed(ss1))
            ss2 = list(reversed(ss2))
            for c1,c2 in zip(reversed(ss1),reversed(ss2)):
                if c1==c2:
                    delta +=1
                    rem.append(ss1.pop())
                    ss2.pop()
                else:
                    break
        return func(ss1,ss2,*args, **kwargs)+delta
    closure._wrapped = func
    return closure


from copy import copy
def gendepth2(size,depth=1,alphab=None):
    """ generate all relevant string of lenght size, with an alphabet of size alphab"""

    if not alphab:
        alphab=depth
    if size<=1:
        for i in range(alphab):
            yield [i]
    else:
        for i in range(alphab):
            for sub in gendepth2(size-1,i+2):
                ll = list(sub)
                l = []
                l.append(i)
                l.extend(copy(ll))
                yield l

lorem = """Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris ac porttitor augue. Sed libero lacus, tristique vel augue ac, elementum suscipit velit. Donec faucibus id sapien vitae convallis. Integer adipiscing dui lectus, sit amet euismod urna viverra at. Praesent cursus ultricies dui, sit amet venenatis tortor malesuada a. Proin iaculis imperdiet massa, quis hendrerit magna. In orci nibh, vehicula non ultrices non, ultricies at ante.

Duis egestas et lorem a iaculis. Mauris justo tellus, suscipit vitae odio quis, aliquet ullamcorper erat. Praesent mattis lacinia suscipit. Donec imperdiet nibh id pretium feugiat. Sed volutpat, mi in tristique ultricies, urna odio tristique nibh, suscipit tempor felis erat at urna. Mauris suscipit tincidunt libero, ut scelerisque ante suscipit sed. Sed sit amet enim eu massa fermentum congue. Mauris in justo mi.

Proin condimentum sed metus quis malesuada. Phasellus lobortis metus eros, ac bibendum ipsum vestibulum a. Quisque eget ante auctor, ultricies odio nec, elementum arcu. Cras vitae lobortis ipsum. Donec luctus urna urna. Donec sit amet augue quis metus faucibus porttitor. Aenean interdum velit sed gravida feugiat. Cras interdum sit amet dolor tempus tempor. Fusce congue sapien at sem sagittis vehicula. Aliquam vulputate nisi consequat metus malesuada molestie ut sit amet lectus. Sed a auctor ipsum. Aenean porta fermentum enim, quis commodo sapien lobortis nec.

Aenean non est nec ipsum lobortis cursus. Vivamus semper consequat aliquam. Cras pretium odio id commodo faucibus. Donec ut dignissim nisi. Cras pellentesque enim nisi, eget pretium tortor venenatis id. Phasellus id luctus est. Phasellus pharetra varius molestie. Sed volutpat felis non elit posuere, quis mollis nunc gravida. Phasellus et fermentum leo. Integer bibendum aliquet elit vel vehicula. Ut vehicula facilisis dui eget adipiscing. Phasellus ut auctor orci, dignissim suscipit dolor. Duis pretium lorem metus. Donec sit amet dictum urna, quis semper arcu. Vestibulum vehicula arcu et ultricies ultrices. Phasellus et dolor arcu.


lorem = ''.join(lorem.split('\n'))
Proin ac metus mi. Cras lacus nisi, varius tempor massa ut, aliquet sodales lacus. Ut id sollicitudin arcu. Cras quis varius massa. Integer cursus justo sed eros vehicula dictum. Donec mattis cursus lectus. Nunc ornare arcu ante, non rhoncus leo rutrum ac. Mauris vel consectetur erat, non posuere magna. Proin tristique viverra dui ac dictum. Etiam egestas enim vel velit dictum cursus. Duis ullamcorper varius lacus vel luctus. Sed tincidunt elit et sapien porttitor rutrum. Etiam nibh mi, convallis ut pretium at, consectetur et velit.

Donec egestas venenatis risus, porta interdum leo dictum ut. Praesent eleifend pellentesque massa, sed condimentum nisi scelerisque faucibus. Nam tincidunt dui purus, ut eleifend turpis consectetur pretium. Nam non blandit velit. Aliquam mattis congue mauris semper ullamcorper. Sed ullamcorper, felis blandit condimentum porttitor, nunc enim placerat ligula, at sagittis velit mi eu nisi. Ut suscipit vulputate mollis. Sed sodales nisi sed libero pulvinar, vel volutpat nisi lacinia. Nam mollis sollicitudin molestie. Fusce sit amet enim id nunc tempor adipiscing ut porta nunc. Sed sed arcu pulvinar, elementum risus et, aliquet orci. Suspendisse eu luctus dui. Vivamus fringilla enim vitae nisl hendrerit dapibus quis vel enim.

Quisque quis sollicitudin orci. In hac habitasse platea dictumst. Aliquam a auctor odio. Mauris venenatis lectus quam, sed sagittis nunc vulputate sed. Morbi urna magna, fermentum quis tortor at, rhoncus porttitor sapien. In quis commodo nunc. Praesent vitae erat sed enim mollis accumsan. Donec in velit vel augue porta fermentum. Nulla dictum, nisl et ullamcorper consectetur, nunc enim placerat nisi, id volutpat sapien turpis sit amet magna. Sed luctus laoreet libero eget luctus.

Cras venenatis quam tortor, a sodales urna laoreet id. Donec faucibus, ante in tincidunt commodo, velit massa tincidunt mi, sed sagittis nulla est id leo. Quisque iaculis vulputate tristique. Quisque iaculis semper egestas. Mauris quam diam, lobortis sit amet interdum eget, facilisis non turpis. Nulla cursus augue sit amet lacus ultricies, id sollicitudin enim congue. Etiam dictum dolor quis mauris tristique facilisis. Quisque ac dictum sapien. Nunc pulvinar purus vel sapien dignissim dictum. Sed malesuada nibh at lacus condimentum hendrerit tempus vitae urna. Nulla vestibulum lacus ante, id ultricies sem placerat ut. Nunc sem enim, dictum dictum neque non, pulvinar ultricies erat. Nulla nec nisi enim. Vivamus sagittis lacinia mi ut auctor. Suspendisse sit amet lacus fermentum, accumsan turpis non, blandit leo.

Suspendisse interdum sapien et tristique eleifend. Quisque venenatis justo a mauris vestibulum dapibus. Quisque ornare posuere blandit. Sed vel eros tempus, sollicitudin massa eget, adipiscing libero. Sed vel dictum erat. Etiam eleifend mi non erat rhoncus mattis. Nam et dolor vitae sem suscipit rhoncus. Praesent quis rhoncus tellus. Praesent ut turpis dolor amet."""


from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import HtmlFormatter
from IPython.display import HTML
import io

def hl(name):
    with io.open(name) as f:
        return HTML(highlight(f.read(), PythonLexer(), HtmlFormatter(noclasses=True)))
