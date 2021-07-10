import pytest

@pytest.mark.usefixtures("setup")
class TestExample:

    def test_firstProgram(self):
        print("Hello")


    # @pytest.mark.skip #this is used to skip the test case
    # @pytest.mark.xfail #This is used for run the test. Result pass or fail does not shows in report
    def test_secondProgram(self):
        print("Good Morning")


    def test_firstProgram1(self):
        msg = "Hello"
        assert msg == "Hi"


    def test_secondProgram2(self):
        a = 4
        b = 6
        assert a + 2 == 6, "Addition Does Not Match"

    # @pytest.fixture()
    # def setup():
    #     print("I will Execute First")


    def test_firstDemo(self):
        print("I will execute steps in fixtureDemo Method")