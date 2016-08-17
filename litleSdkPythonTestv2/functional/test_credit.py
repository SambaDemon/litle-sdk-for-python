import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestCredit:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleCreditWithCard(self, credit_fixture, card_fixture):
        credit = credit_fixture
        card = card_fixture
        credit.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(credit)
        assert(response.message == "Approved")

    def testSimpleCreditWithPaypal(self, credit_fixture):
        credit = credit_fixture
        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        credit.paypal = paypal

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(credit)
        assert(response.message == "Approved")

    def testSimpleCreditWithCardAndSecondaryAmount(
            self, credit_fixture, card_fixture):
        credit = credit_fixture
        credit.secondaryAmount = 10
        card = card_fixture
        credit.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(credit)
        assert(response.message == "Approved")

    def testSimpleCreditWithTxnAndSecondaryAmount(self, credit_txn_fixture):
        credit = credit_txn_fixture
        credit.secondaryAmount = 10

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(credit)
        assert(response.message == "Approved")

    def testSimpleCreditConflictWithTxnAndOrderId(self, credit_fixture):
        credit = credit_fixture
        credit.litleTxnId = "12345"

        litleXml = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litleXml.sendRequest(credit)

    def testPaypalNotes(self, credit_fixture, card_fixture):
        credit = credit_fixture
        credit.payPalNotes = "Hello"
        card = card_fixture
        credit.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(credit)
        assert(response.message == "Approved")

    def testProcessingInstructionAndAmexData(
            self, credit_fixture, card_fixture):
        credit = credit_fixture
        pI = litleXmlFields.processingInstructions()
        pI.bypassVelocityCheck = True
        credit.processingInstructions = pI
        card = card_fixture
        credit.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(credit)

        assert(response.message == "Approved")
