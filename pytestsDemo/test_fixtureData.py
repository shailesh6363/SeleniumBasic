import pytest

from pytestsDemo.BaseClass import baseClass


@pytest.mark.usefixtures("dataload")
class TestExample2(baseClass):

    def test_editProfile(self,dataload):
        log=self.getLogger()
        log.info(dataload)
