
import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestEcheckRedeposit:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleEcheckRedeposit(self):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckredeposit)
        assert(response.message == "Approved")

    def testEcheckRedepositWithEcheck(self, echeck_fixture):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456
        echeck = echeck_fixture
        echeckredeposit.echeck = echeck

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckredeposit)
        assert(response.message == "Approved")

    def testEcheckRedepositWithEcheckToken(self, echeck_token_fixture):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456
        echeckToken = echeck_token_fixture
        echeckredeposit.echeckToken = echeckToken

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckredeposit)
        assert(response.message == "Approved")
