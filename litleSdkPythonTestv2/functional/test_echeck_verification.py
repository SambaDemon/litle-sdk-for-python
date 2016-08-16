import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestEcheckVerification:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleEcheckVerification(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123456
        echeckverification.orderId = '12345'
        echeckverification.orderSource = 'ecommerce'

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeckverification.echeckOrEcheckToken = echeck

        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echeckverification.billToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckverification)
        assert(response.message == "Approved")

    def test_echeckVerificationWithEcheckToken(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123456
        echeckverification.orderId = '12345'
        echeckverification.orderSource = 'ecommerce'

        token = litleXmlFields.echeckToken()
        token.accType = 'Checking'
        token.litleToken = "1234565789012"
        token.routingNum = "123456789"
        token.checkNum = "123455"
        echeckverification.echeckOrEcheckToken = token

        contact = litleXmlFields.contact()
        contact.name = "Bob"
        contact.city = "lowell"
        contact.state = "MA"
        contact.email = "litle.com"
        echeckverification.billToAddress = contact

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(echeckverification)
        assert(response.message == "Approved")

    def test_MissingBillingField(self):
        echeckverification = litleXmlFields.echeckVerification()
        echeckverification.amount = 123
        echeckverification.orderId = '12345'
        echeckverification.orderSource = 'ecommerce'

        echeck = litleXmlFields.echeck()
        echeck.accType = 'Checking'
        echeck.accNum = '12345657890'
        echeck.routingNum = '123456789'
        echeck.checkNum = '123455'
        echeckverification.echeckOrEcheckToken = echeck

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(echeckverification)
