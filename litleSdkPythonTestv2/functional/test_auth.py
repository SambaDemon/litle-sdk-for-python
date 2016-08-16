import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestAuth:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleAuthWithCard(self, auth_fixture, card_fixture):
        authorization = auth_fixture
        card = card_fixture
        authorization.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)
        assert(response.response == "000")

    def testSimpleAuthWithPaypal(self, auth_fixture, paypal_fixture):
        authorization = auth_fixture
        paypal = paypal_fixture
        authorization.paypal = paypal

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)
        assert(response.message == "Approved")

    def testSimpleAuthWithSecondaryAmountAndApplepay(
            self, auth_fixture, applepay_fixture, applepay_header_fixture):
        authorization = auth_fixture
        authorization.secondaryAmount = '10'
        applepay = applepay_fixture
        header = applepay_header_fixture
        applepay.header = header
        authorization.applepay = applepay

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)
        assert(response.message == "Insufficient Funds")
        assert(
            response.applepayResponse.transactionAmount == authorization.amount)

    def testPosWithoutCapabilityAndEntryMode(
            self, auth_fixture, pos_fixture, card_fixture):
        authorization = auth_fixture
        pos = pos_fixture
        card = card_fixture
        authorization.pos = pos
        authorization.card = card

        litleXml = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litleXml.sendRequest(authorization)

    def testAccountUpdate(self, auth_fixture, card_fixture):
        authorization = auth_fixture

        card = card_fixture
        card.number = "4100100000000000"
        card.cardValidationNum = '1213'

        authorization.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)

        assert(response.accountUpdater.originalCardInfo.number == card.number)

    def testTrackData(self):
        authorization = litleXmlFields.authorization()
        authorization.id = 'AX54321678'
        authorization.reportGroup = 'RG27'
        authorization.orderId = '12z58743y1'
        authorization.amount = 12522
        authorization.orderSource = 'retail'

        billToAddress = litleXmlFields.contact()
        billToAddress.zip = '95032'
        authorization.billToAddress = billToAddress

        card = litleXmlFields.cardType()
        card.track = "%B40000001^Doe/JohnP^06041...?;40001=0604101064200?"
        authorization.card = card

        pos = litleXmlFields.pos()
        pos.capability = 'magstripe'
        pos.entryMode = 'completeread'
        pos.cardholderId = 'signature'
        authorization.pos = pos

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)

        assert(response.message == 'Approved')

    def testListOfTaxAmounts(self, auth_fixture, card_fixture):
        authorization = auth_fixture
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.amount = 10000

        enhanced = litleXmlFields.enhancedData()
        dt1 = litleXmlFields.detailTax()
        dt1.taxAmount = 100
        enhanced.detailTax.append(dt1)
        dt2 = litleXmlFields.detailTax()
        dt2.taxAmount = 200
        enhanced.detailTax.append(dt2)
        authorization.enhancedData = enhanced

        card = card_fixture
        authorization.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)

        assert(response.message == 'Approved')
