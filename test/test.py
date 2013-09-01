import difflib2


def test1():
    assert difflib2.lcs('foo','foo') == 'foo'
