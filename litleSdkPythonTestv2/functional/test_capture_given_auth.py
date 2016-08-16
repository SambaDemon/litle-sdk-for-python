import pytest
import pyxb
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestCaptureGivenAuth:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config
        self.config.printXml = True

    def testSimpleCaptureGivenAuth(self):
        import ipdb; ipdb.set_trace() # DEBUG
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 20)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        CaptureGivenAuth.orderSource = "ecommerce"
        Card = litleXmlFields.cardType()
        Card.number = "4100000000000000"
        Card.expDate = "1210"
        Card.type = 'VI'
        Card.cardValidationNum = '1210'
        CaptureGivenAuth.card = Card
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        assert(response.message == "Approved")

    def testSimpleCaptureGivenAuthWithToken(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        CaptureGivenAuth.orderSource = "ecommerce"
        Token = litleXmlFields.cardTokenType()
        Token.litleToken = "123456789101112"
        Token.expDate = "1210"
        Token.type = 'VI'
        Token.cardValidationNum = '555'
        CaptureGivenAuth.token = Token
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        assert(response.message == "Approved")

    def testComplexCaptureGivenAuth(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.secondaryAmount = 10
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        CaptureGivenAuth.authInformation = AuthInfo
        Contact = litleXmlFields.contact()
        Contact.name = "Bob"
        Contact.city = "lowell"
        Contact.state = "MA"
        Contact.email = "litle.com"
        CaptureGivenAuth.billToAddress = Contact
        ProcessingInstruct = litleXmlFields.processingInstructions()
        ProcessingInstruct.bypassVelocityCheck = True
        CaptureGivenAuth.processingInstructions = ProcessingInstruct
        CaptureGivenAuth.orderSource = "ecommerce"
        Card = litleXmlFields.cardType()
        Card.number = "4100000000000000"
        Card.expDate = "1210"
        Card.type = 'VI'
        Card.cardValidationNum = '1210'
        CaptureGivenAuth.card = Card
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        assert(response.message == "Approved")

    def testAuthInfo(self):
        CaptureGivenAuth = litleXmlFields.captureGivenAuth()
        CaptureGivenAuth.amount = 106
        CaptureGivenAuth.orderId = "12344"
        AuthInfo = litleXmlFields.authInformation()
        date = pyxb.binding.datatypes.date(2002, 10, 9)
        AuthInfo.authDate = date
        AuthInfo.authCode = "543216"
        AuthInfo.authAmount = 12345
        FraudResult = litleXmlFields.fraudResult()
        FraudResult.avsResult = "12"
        FraudResult.cardValidationResult = "123"
        FraudResult.authenticationResult = "1"
        FraudResult.advancedAvsResult = "123"
        AuthInfo.fraudResult = FraudResult
        CaptureGivenAuth.authInformation = AuthInfo
        CaptureGivenAuth.orderSource = "ecommerce"
        Card = litleXmlFields.cardType()
        Card.number = "4100000000000000"
        Card.expDate = "1210"
        Card.type = 'VI'
        Card.cardValidationNum = '555'
        CaptureGivenAuth.card = Card
        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(CaptureGivenAuth)
        assert(response.message == "Approved")
