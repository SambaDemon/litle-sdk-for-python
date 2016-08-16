import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestForceCapture:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleForceCaptureWithCard(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106
        forcecapture.orderId = '12344'
        forcecapture.orderSource = 'ecommerce'

        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        forcecapture.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(forcecapture)
        assert(response.message == "Approved")

    def testSimpleForceCaptureWithToken(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106
        forcecapture.orderId = '12344'
        forcecapture.orderSource = 'ecommerce'

        token = litleXmlFields.cardTokenType()
        token.type = 'VI'
        token.expDate = "1210"
        token.litleToken = "123456789101112"
        token.cardValidationNum = "555"
        forcecapture.token = token

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(forcecapture)
        assert(response.message == "Approved")

    def testSimpleForceCaptureWithSecondaryAmount(self):
        forcecapture = litleXmlFields.forceCapture()
        forcecapture.amount = 106
        forcecapture.secondaryAmount = 10
        forcecapture.orderId = '12344'
        forcecapture.orderSource = 'ecommerce'

        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4100000000000001"
        card.expDate = "1210"
        forcecapture.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(forcecapture)
        assert(response.message == "Approved")
