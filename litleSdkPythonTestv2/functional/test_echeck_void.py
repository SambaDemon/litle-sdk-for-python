import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestEcheckVoid:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testTestEcheckVoid(self):
        echeckvoid = litleXmlFields.echeckVoid()
        echeckvoid.litleTxnId = 123456789101112
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckvoid)
        assert(response.message == "Approved")
