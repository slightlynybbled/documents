import pytest
from documents.fields import *


def test_field_creation():
    f = Field()

    assert f


def test_field_validation():
    f = Field(required=True)

    assert(f.validate('test string'))

    with pytest.raises(ValueError):
        f.validate(None)


def test_stringfield_creation():
    sf = StringField()
    assert sf
    assert sf.validate(None)


def test_stringfield_validation():
    sf = StringField(min_length=2, max_length=15)

    assert sf.validate('test string')

    with pytest.raises(ValueError):
        sf.validate(37)
    with pytest.raises(ValueError):
        sf.validate(True)
    with pytest.raises(ValueError):     # min string length
        sf.validate('1')
    with pytest.raises(ValueError):
        sf.validate('1234567890123456') # max string length


def test_boolfield_creation():
    bf = BooleanField()
    assert bf


def test_boolfield_validation():
    bf = BooleanField()

    assert bf.validate(True)

    with pytest.raises(ValueError):
        bf.validate('string input')
    with pytest.raises(ValueError):
        bf.validate(10)


def test_intfield_creation():
    intf = IntField()
    assert intf


def test_intfield_validation():
    intf = IntField(max_value=100)

    assert intf.validate(10)

    with pytest.raises(ValueError):
        intf.validate(101)

    with pytest.raises(ValueError):
        intf.validate('10')

    with pytest.raises(ValueError):
        intf.validate(10.0)
