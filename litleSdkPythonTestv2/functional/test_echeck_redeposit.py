
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

    def testEcheckRedepositWithEcheck(self):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echeckredeposit.echeck = echeck

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckredeposit)
        assert(response.message == "Approved")

    def testEcheckRedepositWithEcheckToken(self):
        echeckredeposit = litleXmlFields.echeckRedeposit()
        echeckredeposit.litleTxnId = 123456

        echeckToken = litleXmlFields.echeckTokenType()
        echeckToken.litleToken = "1234565789012"
        echeckToken.routingNum = "123456789"
        echeckToken.checkNum = "123455"
        echeckredeposit.echeckToken = echeckToken

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckredeposit)
        assert(response.message == "Approved")
