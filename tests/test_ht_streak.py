# https://code.visualstudio.com/docs/python/testing

from .context import exercises
from exercises import ht_streak


def test_generate_string():
    # test length of 5 = 9 (5 results and 4 spaces between)
    n = 5
    result_length = n + (n-1)
    assert len(ht_streak.generate_string(n)) == result_length
    # Try length of 100 is 199
    n = 100
    result_length = n + (n-1)
    assert len(ht_streak.generate_string(n)) == result_length
    # Test default length is 10
    n = 10
    result_length = n + (n-1)
    # this time, don't pass n and rely on the default
    assert len(ht_streak.generate_string()) == result_length


def test_streaks_in_string():
    assert ht_streak.streaks_in_string('H T H T H') == 0
    assert ht_streak.streaks_in_string('H H H H H', 4) == 1
    assert ht_streak.streaks_in_string('H H T H H', 2) == 2
    assert ht_streak.streaks_in_string('H H T H H T H H', 2) == 3
    assert ht_streak.streaks_in_string('H H T T H H T T', 2) == 4
