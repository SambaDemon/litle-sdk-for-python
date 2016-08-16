import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestEcheckSale:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleEcheckSaleWithEcheck(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echecksale.echeckOrEcheckToken = echeck

        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
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

    def testEcheckSaleWithShipTo(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.amount = 123456
        echecksale.verify = True
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echecksale.echeckOrEcheckToken = echeck

        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact
        echecksale.shipToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echecksale)
        assert(response.message == "Approved")

    def testEcheckSaleWithEcheckToken(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.amount = 123456
        echecksale.verify = True
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'

        token = litleXmlFields.echeckToken()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum = "123455"
        echecksale.echeckOrEcheckToken = token

        custombilling = litleXmlFields.customBilling()
        custombilling.phone = "123456789"
        custombilling.descriptor = "good"
        echecksale.customBilling = custombilling

        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echecksale)
        assert(response.message == "Approved")

    def testEcheckSaleWithSecoundaryAmountAndCCD(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.amount = 123456
        echecksale.secondaryAmount = 10
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echeck.ccdPaymentInformation = \
            "1234567890123456789012345678901234" + \
            "5678901234567890123456789012345678901234567890"
        echecksale.echeckOrEcheckToken = echeck

        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echecksale.billToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echecksale)
        assert(response.message == "Approved")

    def testEcheckSaleMissingBilling(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.amount = 123456

        token = litleXmlFields.echeckTokenType()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum = "123455"
        echecksale.echeckToken = token

        echecksale.verify = True
        echecksale.orderId = "12345"
        echecksale.orderSource = 'ecommerce'

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(echecksale)

    def testSimpleEcheckSale(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.litleTxnId = 123456789101112
        echecksale.amount = 12

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echecksale)
        assert(response.message == "Approved")

    def testEcheckSaleWithLitleTxnIdAndSecondryAmount(self):
        echecksale = litleXmlFields.echeckSale()
        echecksale.reportGroup = "Planets"
        echecksale.litleTxnId = 123456789101112
        echecksale.amount = 12
        echecksale.secondaryAmount = 10

        litleXml = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litleXml.sendRequest(echecksale)
