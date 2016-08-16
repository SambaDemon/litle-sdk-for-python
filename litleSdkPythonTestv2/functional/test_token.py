import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestToken:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleToken(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        token.accountNumber = '1233456789103801'
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(token)
        assert(response.message == "Account number was successfully registered")

    def testSimpleTokenWithPaypage(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        token.paypageRegistrationId = '1233456789101112'
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(token)
        assert(response.message == "Account number was successfully registered")

    def testSimpleTokenWithEcheck(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.accNum = "12344565"
        echeck.routingNum = "123476545"
        token.echeckForToken = echeck
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(token)
        assert(response.message == "Account number was successfully registered")

    def testSimpleTokenWithApplepay(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "sign"
        applepay.version = '1'
        header = litleXmlFields.applepayHeaderType()
        header.applicationData = \
            'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.ephemeralPublicKey = \
            'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.publicKeyHash = \
            'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
        header.transactionId = '1024'
        applepay.header = header
        token.applepay = applepay
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(token)
        assert(response.message == "Account number was successfully registered")
        assert(response.applepayResponse.transactionAmount == 0)

    def testTokenEcheckMissingRequiredField(self):
        token = litleXmlFields.registerTokenRequest()
        token.orderId = '12344'
        echeck = litleXmlFields.echeckForTokenType()
        echeck.routingNum = "123476545"
        token.echeckForToken = echeck

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(token)

    def testCovertPaypageRegistrationIdIntoToken(self):
        tokenRequest = litleXmlFields.registerTokenRequest()
        tokenRequest.orderId = '12345'
        tokenRequest.paypageRegistrationId = \
            '123456789012345678901324567890abcdefghi'

        litleXml = litleOnlineRequest(self.config)
        tokenResponse = litleXml.sendRequest(tokenRequest)
        assert(tokenResponse.litleToken == "1111222233334444")
