import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestEcheckSale:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleEcheckSaleWithEcheck(
            self, echeck_sale_fixture, echeck_fixture, contact_fixture):
        echecksale = echeck_sale_fixture
        echeck = echeck_fixture
        echecksale.echeckOrEcheckToken = echeck
        contact = contact_fixture
        echecksale.billToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echecksale)
        assert(response.message == "Approved")

    def testNoAmount(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(echecksale)

    def testEcheckSaleWithShipTo(
            self, echeck_sale_fixture, echeck_fixture, contact_fixture):
        echecksale = echeck_sale_fixture
        echecksale.reportGroup = "Planets"
        echecksale.verify = True
        echeck = echeck_fixture
        echecksale.echeckOrEcheckToken = echeck
        contact = contact_fixture
        echecksale.billToAddress = contact
        echecksale.shipToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echecksale)
        assert(response.message == "Approved")

    def testEcheckSaleWithEcheckToken(
            self, echeck_sale_fixture, echeck_token_fixture, contact_fixture):
        echecksale = echeck_sale_fixture
        echecksale.reportGroup = "Planets"
        echecksale.verify = True
        token = echeck_token_fixture
        echecksale.echeckOrEcheckToken = token

        custombilling = litleXmlFields.customBilling()
        custombilling.phone = "123456789"
        custombilling.descriptor = "good"
        echecksale.customBilling = custombilling

        contact = contact_fixture
        echecksale.billToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echecksale)
        assert(response.message == "Approved")

    def testEcheckSaleWithSecoundaryAmountAndCCD(
            self, echeck_sale_fixture, echeck_fixture, contact_fixture):
        echecksale = echeck_sale_fixture
        echecksale.secondaryAmount = 10
        echeck = echeck_fixture
        echeck.ccdPaymentInformation = \
            "1234567890123456789012345678901234" + \
            "5678901234567890123456789012345678901234567890"
        echecksale.echeckOrEcheckToken = echeck
        contact = contact_fixture
        echecksale.billToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echecksale)
        assert(response.message == "Approved")

    def testEcheckSaleMissingBilling(
            self, echeck_sale_fixture, echeck_token_fixture):
        echecksale = echeck_sale_fixture
        echecksale.reportGroup = "Planets"
        echecksale.verify = True
        token = echeck_token_fixture
        echecksale.echeckToken = token

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(echecksale)

    def testSimpleEcheckSale(self, echeck_sale_txn_fixture):
        echecksale = echeck_sale_txn_fixture
        echecksale.reportGroup = "Planets"

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echecksale)
        assert(response.message == "Approved")

    def testEcheckSaleWithLitleTxnIdAndSecondryAmount(
            self, echeck_sale_txn_fixture):
        echecksale = echeck_sale_txn_fixture
        echecksale.reportGroup = "Planets"
        echecksale.secondaryAmount = 10

        litleXml = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litleXml.sendRequest(echecksale)
