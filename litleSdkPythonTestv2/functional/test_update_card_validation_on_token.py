import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestUpdateCardValidationOnToken:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimple(self):
        update = litleXmlFields.updateCardValidationNumOnToken()
        update.litleToken = '1111222233334444'
        update.cardValidationNum = '123'

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(update)
        assert(response.response == "805")
