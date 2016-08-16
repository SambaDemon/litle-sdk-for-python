import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestEcheckCredit:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleEcheckCredit(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.litleTxnId = 123456789101112

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testNoLitleTxnId(self):
        echeckCredit = litleXmlFields.echeckCredit()

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(echeckCredit)

    def testEcheckCreditWithEcheck(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.orderId = "12345"
        echeckCredit.orderSource = 'ecommerce'

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echeckCredit.echeckOrEcheckToken = echeck

        billToAddress = litleXmlFields.contact()
        billToAddress.name = "Bob"
        billToAddress.City = "Lowell"
        billToAddress.State = "MA"
        billToAddress.email = "litle.com"
        echeckCredit.billToAddress = billToAddress

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testEcheckCreditWithSecondryAmount(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.secondaryAmount = 10
        echeckCredit.orderId = "12345"
        echeckCredit.orderSource = 'ecommerce'

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echeckCredit.echeckOrEcheckToken = echeck

        billToAddress = litleXmlFields.contact()
        billToAddress.name = "Bob"
        billToAddress.City = "Lowell"
        billToAddress.State = "MA"
        billToAddress.email = "litle.com"
        echeckCredit.billToAddress = billToAddress

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testEcheckCreditWithLitleTxnIdAndSecondryAmount(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.litleTxnId = 123456789101112
        echeckCredit.secondaryAmount = 10

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testEcheckCreditWithToken(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.orderId = "12345"
        echeckCredit.orderSource = 'ecommerce'

        token = litleXmlFields.echeckToken()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum = "123455"
        echeckCredit.echeckOrEcheckToken = token

        billToAddress = litleXmlFields.contact()
        billToAddress.name = "Bob"
        billToAddress.City = "Lowell"
        billToAddress.State = "MA"
        billToAddress.email = "litle.com"
        echeckCredit.billToAddress = billToAddress

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckCredit)
        assert(response.message == "Approved")

    def testMissingBilling(self):
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 12
        echeckCredit.orderId = "12345"
        echeckCredit.orderSource = 'ecommerce'

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = "1234567890"
        echeck.routingNum = "123456789"
        echeck.checkNum = "123455"
        echeckCredit.echeckOrEcheckToken = echeck

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(echeckCredit)
