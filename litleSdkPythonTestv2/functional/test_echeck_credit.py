import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestEcheckCredit:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleEcheckCredit(self, echeck_credit_txn_fixture):
        echeckCredit = echeck_credit_txn_fixture

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testNoLitleTxnId(self):
        echeckCredit = litleXmlFields.echeckCredit()

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(echeckCredit)

    def testEcheckCreditWithEcheck(
            self, echeck_credit_fixture, echeck_fixture, contact_fixture):
        echeckCredit = echeck_credit_fixture
        echeck = echeck_fixture
        echeckCredit.echeckOrEcheckToken = echeck
        billToAddress = contact_fixture
        echeckCredit.billToAddress = billToAddress

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testEcheckCreditWithSecondryAmount(
            self, echeck_credit_fixture, echeck_fixture, contact_fixture):
        echeckCredit = echeck_credit_fixture
        echeckCredit.secondaryAmount = 10
        echeck = echeck_fixture
        echeckCredit.echeckOrEcheckToken = echeck
        billToAddress = contact_fixture
        echeckCredit.billToAddress = billToAddress

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testEcheckCreditWithLitleTxnIdAndSecondryAmount(
            self, echeck_credit_txn_fixture):
        echeckCredit = echeck_credit_txn_fixture
        echeckCredit.secondaryAmount = 10

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testEcheckCreditWithToken(
            self, echeck_credit_fixture, echeck_token_fixture, contact_fixture):
        echeckCredit = echeck_credit_fixture
        token = echeck_token_fixture
        echeckCredit.echeckOrEcheckToken = token
        billToAddress = contact_fixture
        echeckCredit.billToAddress = billToAddress

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testMissingBilling(self, echeck_credit_fixture, echeck_fixture):
        echeckCredit = echeck_credit_fixture
        echeck = echeck_fixture
        echeckCredit.echeckOrEcheckToken = echeck

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(echeckCredit)
