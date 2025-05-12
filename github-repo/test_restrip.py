from restrip import strip

def test_strip():
    assert strip('  blah   ')=='blah'
    assert strip('\tfoo  \n')=='foo'
    assert strip('eagdekoo','aeiou')=='gdek'
    assert strip('338alpha 90','0123456789')=='alpha '
