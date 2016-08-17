import pytest
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestEcheckVerification:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleEcheckVerification(
            self, echeck_verfication_fixture, echeck_fixture, contact_fixture):
        echeckverification = echeck_verfication_fixture
        echeck = echeck_fixture
        echeckverification.echeckOrEcheckToken = echeck
        contact = contact_fixture
        echeckverification.billToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckverification)
        assert(response.message == "Approved")

    def test_echeckVerificationWithEcheckToken(
            self, echeck_verfication_fixture,
            echeck_token_fixture, contact_fixture):
        echeckverification = echeck_verfication_fixture
        token = echeck_token_fixture
        echeckverification.echeckOrEcheckToken = token
        contact = contact_fixture
        echeckverification.billToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckverification)
        assert(response.message == "Approved")

    def test_MissingBillingField(
            self, echeck_verfication_fixture, echeck_fixture):
        echeckverification = echeck_verfication_fixture
        echeck = echeck_fixture
        echeckverification.echeckOrEcheckToken = echeck

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(echeckverification)
