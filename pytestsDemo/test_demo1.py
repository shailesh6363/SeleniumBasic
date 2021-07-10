# Any Pytest file should start with test
# Pytest Method names should start with test and end with _test
import pytest


@pytest.mark.smoke
def test_firstProgram(setup):
    print("Hello")


@pytest.mark.smoke
#@pytest.mark.skip #this is used to skip the test case
#@pytest.mark.xfail #This is used for run the test. Result pass or fail does not shows in report
def test_secondProgram(setup):
    print("Good Morning")

@pytest.mark.smoke
def test_crossBrowser(crossBrowser):
    print(crossBrowser)