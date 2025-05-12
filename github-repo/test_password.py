from password import check

def test_check():
    assert check('12345')==False
    assert check('eeeeeeeeee')==False
    assert check('Far1')==False
    assert check('2Fast2caTch')==True
    assert check('g4rrplanet')==False
    assert check('g4rrplaneT')==True
    assert check('5592592609')==False
    assert check('PARKING0SSIP')==False
    assert check('PARKiNG0SSIP')==True
