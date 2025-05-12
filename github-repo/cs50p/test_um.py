from um import count

def test_no_um():
    assert count('hello world')==0
    assert count('50')==0

def test_um_in_word():
    assert count('lithium')==0
    assert count('i have an umbrella')==0
    assert count('the sum of 1 and 5 is 6')==0
    assert count('circumstances')==0

def test_solitary_um():
    assert count('um')==1
    assert count('um?')==1
    assert count('um, i don\'t think so')==1
    assert count('fjsd um slp um b')==2
    assert count('so, um... i, um, took the, um, dog for a, um, walk')==4
