import pytest
from mypackage import module


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


def test_add_five_simple(val=5):
    """Test that 5 is addded to the input value

    In ths test we just pass a single value as a parameter
    """
    assert module.add_five(val) == 10 

@pytest.mark.parametrize("val, expected_output", [(1,6),(2,7),(4.5,9.5)])
def test_add_five_multiple(val, expected_output):
    """Send in multiple inputs for testing

    This test uses the parametrize decorator in pytest to
    Send in multipl values  for input into the function.
    A new test is created for each pair of input and expected output

    Parameters
    ----------
    val : number
        Input value that should be an integer or float

    expected_output: number
        The expected return from the add_five function in module

    Notes
    -----
    and executed. If you run pytest --collect-only you shoud s

    collected 8 items                                                                                                                                                  

            <Dir example_package>
              <Package mypackage>
                <Package tests>
                  <Module test_basic.py>
                    <Function test_always_passes>
                    <Function test_always_fails>
                    <Function test_reversed>
                    <Function test_with_fixture>
                    <Function test_add_five_simple>
                    <Function test_add_five_multiple[1-6]>
                    <Function test_add_five_multiple[2-7]>
                    <Function test_add_five_multiple[4-9]>

    """
    assert module.add_five(val) == expected_output

