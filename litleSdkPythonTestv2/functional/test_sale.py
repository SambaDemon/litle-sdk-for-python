import pytest
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestSale:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleSaleWithCard(self, sale_fixture, card_fixture):
        sale = sale_fixture
        card = card_fixture
        # It's a magic number, because other will return "Approved" message
        card.number = "4100000000000001"
        sale.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(sale)
        assert(response.message == "Transaction Received")

    def testSimpleSaleWithPayPal(self, sale_fixture, paypal_fixture):
        sale = sale_fixture
        paypal = paypal_fixture
        sale.paypal = paypal

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(sale)
        assert(response.message == "Approved")

    def testSimpleSaleWithToken(self, sale_fixture, card_token_fixture):
        sale = sale_fixture
        token = card_token_fixture
        sale.token = token

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(sale)
        assert(response.message == "Approved")

    def testSimpleSaleWithSecondaryAmountAndApplepay(
            self, sale_fixture, applepay_fixture, applepay_header_fixture):
        sale = sale_fixture
        sale.secondaryAmount = 10
        applepay = applepay_fixture
        header = applepay_header_fixture
        applepay.header = header
        sale.applepay = applepay

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(sale)
        assert(response.message == "Approved")
        assert(response.applepayResponse.transactionAmount == sale.amount)
