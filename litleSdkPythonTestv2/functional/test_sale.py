import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestSale:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleSaleWithCard(self):
        sale = litleXmlFields.sale()
        sale.litleTxnId = 123456
        sale.amount = 106
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'

        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        sale.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(sale)
        assert(response.message == "Transaction Received")

    def testSimpleSaleWithPayPal(self):
        sale = litleXmlFields.sale()
        sale.litleTxnId = 123456
        sale.amount = 106
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'

        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        paypal.token = "1234"
        paypal.transactionId = "123456"
        sale.paypal = paypal

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(sale)
        assert(response.message == "Approved")

    def testSimpleSaleWithToken(self):
        sale = litleXmlFields.sale()
        sale.amount = 106
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'
        token = litleXmlFields.cardTokenType()
        token.cardValidationNum = '349'
        token.expDate = '1214'
        token.litleToken = '1111222233334000'
        token.type = 'VI'
        sale.token = token

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(sale)
        assert(response.message == "Approved")

    def testSimpleSaleWithSecondaryAmountAndApplepay(self):
        sale = litleXmlFields.sale()
        sale.litleTxnId = 123456
        sale.amount = 106
        sale.secondaryAmount = 10
        sale.orderId = '12344'
        sale.orderSource = 'ecommerce'

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
        sale.applepay = applepay

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(sale)
        assert(response.message == "Approved")
        assert(response.applepayResponse.transactionAmount == 106)
