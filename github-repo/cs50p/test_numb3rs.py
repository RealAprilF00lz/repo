from numb3rs import validate

def test_not_even_close():
    assert validate('cat')==False
    assert validate('42')==False

def test_not_numbers():
    assert validate('cat.dog.it.go')==False

def test_wrong_delimiter():
    assert validate('10?0?44?201')==False
    assert validate('23..56..40..100')==False

def test_more_than_255():
    assert validate('256.0.50.1')==False
    assert validate('10.500.20.4')==False

def test_negative():
    assert validate('40.-2.107.10')==False

def test_extra_text():
    assert validate('30.99.11.190.')==False
    assert validate('h20.240.60.1e')==False

def test_correct():
    assert validate('10.0.255.4')==True
    assert validate('1.2.3.4')==True
