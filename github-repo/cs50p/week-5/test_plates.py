from plates import is_valid

def test_valid_inputs():
    assert is_valid('CS50')==True
    assert is_valid('CS5')==True
    assert is_valid('CS')==True
    assert is_valid('CS5005')==True

def test_length():
    assert is_valid('HELLO50')==False
    assert is_valid('H')==False

def test_leading_alphabetical():
    assert is_valid('C554')==False

def test_isalnum():
    assert is_valid('CS5-0')==False
    assert is_valid('CS50!')==False

def test_num_not_in_middle():
    assert is_valid('CS50P')==False

def test_first_num_not_zero():
    assert is_valid('CS05')==False


