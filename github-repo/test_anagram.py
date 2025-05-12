from anagram import isanagram

def test_isanagram():
    assert isanagram('f','f')==True
    assert isanagram('f','e')==False
    assert isanagram('listen','silent')==True
    assert isanagram('Save','Vase')==True
    assert isanagram('I am Lord Voldemort!','Tom Marvolo Riddle')==True
    assert isanagram('I am Lord Voldemort!','I am Tom Marvolo Riddle')==False
    assert isanagram('eee','ee')==False
    assert isanagram('ee','eee')==False
    assert isanagram('3below','b3lowe')==True
    assert isanagram('b3lowe','3below')==True
    assert isanagram('3below','b3low')==False
    assert isanagram('CS50','05SC')==True
    assert isanagram('CS50','005SC')==False
    assert isanagram('  . /pos ?? t! ','...stop}{ _')==True
