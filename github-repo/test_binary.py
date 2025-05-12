from binary import binary_to_decimal
from pytest import raises

def test_invalid_input():
    with raises(ValueError):
        binary_to_decimal('cat')
    with raises(ValueError):
        binary_to_decimal('50')
    with raises(TypeError):
        binary_to_decimal(1010)

def test_valid_input():
    assert binary_to_decimal('1010')==10
    assert binary_to_decimal('  1101 ')==13
    assert binary_to_decimal('001100101011')==811

