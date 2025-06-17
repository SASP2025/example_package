import pytest


def test_always_passes():
    assert True

# this checks that the assertion is raises the exception
# correctly, so the test shows a fail but the tests as a
# whole pass because the failure was expected. If you just have the
# assert False statement, it will fail. This is to help
# you think about what the test is looking for and
# how you define pass vs fail in different cases
def test_always_fails():
    with pytest.raises(AssertionError):
        assert False

def test_reversed():
    assert list(reversed([1, 2, 3, 4])) == [4, 3, 2, 1]


# this fixture lives in conftest.py
def test_with_fixture(example_fixture):
    assert example_fixture == 1
