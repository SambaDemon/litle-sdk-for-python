import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestAuth:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleAuthWithCard(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'

        card = litleXmlFields.cardType()
        card.number = "4100000000000000"
        card.expDate = "1210"
        card.type = 'VI'

        authorization.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)
        assert("000" == response.response)

    def testSimpleAuthWithPaypal(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'

        paypal = litleXmlFields.payPal()
        paypal.payerId = "1234"
        paypal.token = "1234"
        paypal.transactionId = '123456'

        authorization.paypal = paypal

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)
        assert("Approved" == response.message)

    def testSimpleAuthWithSecondaryAmountAndApplepay(self):

        authorization = litleXmlFields.authorization()
        authorization.orderId = '1234'
        authorization.amount = 110
        authorization.orderSource = 'ecommerce'
        authorization.secondaryAmount = '10'

        applepay = litleXmlFields.applepayType()
        applepay.data = "4100000000000000"
        applepay.signature = "sign"
        applepay.version = '1'
        header = litleXmlFields.applepayHeaderType()
        header.applicationData = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' # noqa
        header.ephemeralPublicKey ='e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' # noqa
        header.publicKeyHash = 'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855' # noqa
        header.transactionId = '1024'
        applepay.header = header
        authorization.applepay = applepay

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)

        assert("Insufficient Funds" == response.message)
        assert(110 == response.applepayResponse.transactionAmount)

    def testPosWithoutCapabilityAndEntryMode(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '123456'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'

        pos = litleXmlFields.pos()
        pos.cardholderId = "pin"
        authorization.pos = pos

        card = litleXmlFields.cardType()
        card.number = "4100000000000002"
        card.expDate = "1210"
        card.type = 'VI'
        card.cardValidationNum = '1213'

        authorization.card = card

        litle = litleOnlineRequest(self.config)
        with pytest.raises(Exception):
            litle.sendRequest(authorization)

    def testAccountUpdate(self):
        authorization = litleXmlFields.authorization()
        authorization.orderId = '12344'
        authorization.amount = 106
        authorization.orderSource = 'ecommerce'

        card = litleXmlFields.cardType()
        card.number = "4100100000000000"
        card.expDate = "1210"
        card.type = 'VI'
        card.cardValidationNum = '1213'

        authorization.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)

        assert("4100100000000000" ==
               response.accountUpdater.originalCardInfo.number)

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

        assert('Approved' == response.message)

    def testListOfTaxAmounts(self):
        authorization = litleXmlFields.authorization()
        authorization.id = '12345'
        authorization.reportGroup = 'Default'
        authorization.orderId = '67890'
        authorization.amount = 10000
        authorization.orderSource = 'ecommerce'

        enhanced = litleXmlFields.enhancedData()
        dt1 = litleXmlFields.detailTax()
        dt1.taxAmount = 100
        enhanced.detailTax.append(dt1)
        dt2 = litleXmlFields.detailTax()
        dt2.taxAmount = 200
        enhanced.detailTax.append(dt2)
        authorization.enhancedData = enhanced

        card = litleXmlFields.cardType()
        card.number = '4100000000000000'
        card.expDate = '1215'
        card.type = 'VI'
        authorization.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(authorization)

        assert('Approved' == response.message)
