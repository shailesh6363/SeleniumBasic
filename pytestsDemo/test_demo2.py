import pytest

@pytest.mark.smoke
def test_firstProgram(setup):
    msg="Hello"
    assert msg=="Hi"

@pytest.mark.smoke
def test_secondProgram(setup):
    a=4
    b=6
    assert a+2==6, "Addition Does Not Match"


# @pytest.fixture()
# def setup():
#     print("I will Execute First")


@pytest.mark.smoke
def test_firstDemo(setup):
    print("I will execute steps in fixtureDemo Method")