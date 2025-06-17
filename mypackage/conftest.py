import pytest

"""
You can run the tests in the test directory,
by executing pytest from the top of the repository

run all tests it finds: pytest
discover tests and report them, but dont run: pytest --collect-only
"""
@pytest.fixture
def example_fixture():
    return 1