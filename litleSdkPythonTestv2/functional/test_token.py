import pytest
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestToken:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleToken(self, register_token_fixture):
        token = register_token_fixture
        token.accountNumber = '1233456789103801'
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(token)
        assert(response.message == "Account number was successfully registered")

    def testSimpleTokenWithPaypage(self, register_token_fixture):
        token = register_token_fixture
        token.paypageRegistrationId = '1233456789101112'
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(token)
        assert(response.message == "Account number was successfully registered")

    def testSimpleTokenWithEcheck(
            self, register_token_fixture, echeck_for_token_fixture):
        token = register_token_fixture
        echeck = echeck_for_token_fixture
        token.echeckForToken = echeck
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(token)
        assert(response.message == "Account number was successfully registered")

    def testSimpleTokenWithApplepay(
            self, register_token_fixture,
            applepay_fixture, applepay_header_fixture):
        token = register_token_fixture
        applepay = applepay_fixture
        header = applepay_header_fixture
        applepay.header = header
        token.applepay = applepay
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(token)
        assert(response.message == "Account number was successfully registered")
        assert(response.applepayResponse.transactionAmount == 0)

    def testTokenEcheckMissingRequiredField(
            self, register_token_fixture, echeck_for_token_fixture):
        token = register_token_fixture
        echeck = echeck_for_token_fixture
        echeck.accNum = None
        token.echeckForToken = echeck

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(token)

    def testCovertPaypageRegistrationIdIntoToken(self, register_token_fixture):
        tokenRequest = register_token_fixture
        tokenRequest.paypageRegistrationId = \
            '123456789012345678901324567890abcdefghi'

        litleXml = litleOnlineRequest(self.config)
        tokenResponse = litleXml.sendRequest(tokenRequest)
        assert(tokenResponse.litleToken == "1111222233334444")
