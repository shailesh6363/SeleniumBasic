import pytest


@pytest.fixture(scope="class")#after passing this fixture will execute before test execution started and after execution of all
#test cases is completed
def setup():
    print("Test Execution Is Started")
    yield
    print("Test Execution Is Completed")

@pytest.fixture()
def dataload():
    print("user profile data is being created")
    return ["Rahul","Shetty","rahulshettyacadmy.com"]


@pytest.fixture(params=["chrome","firefox","IE"])
def crossBrowser(request):
    return request.param