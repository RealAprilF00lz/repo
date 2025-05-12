from twttr import shorten

def test_twttr():
    assert shorten('Hello World')=='Hll Wrld'
    assert shorten('HELLO WORLD')=='HLL WRLD'
