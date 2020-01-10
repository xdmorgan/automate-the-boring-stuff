# https://code.visualstudio.com/docs/python/testing

from .context import mymodule


def test_increment():
    assert mymodule.inc_dec.increment(3) == 4


def test_decrement():
    assert mymodule.inc_dec.decrement(3) == 2
