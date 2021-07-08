import pytest

@pytest.mark.smoke
def test_firstProgram():
    msg="Hello"
    assert msg=="Hi"

@pytest.mark.smoke
def test_secondProgram():
    a=4
    b=6
    assert a+2==6, "Addition Does Not Match"
