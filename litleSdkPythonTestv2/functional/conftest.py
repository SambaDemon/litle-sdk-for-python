from pytest import fixture
from litleSdkPython import litleXmlFields


@fixture()
def auth_fixture():
    authorization = litleXmlFields.authorization()
    authorization.orderId = '1234'
    authorization.amount = 110
    authorization.orderSource = 'ecommerce'

    return authorization


@fixture()
def card_fixture():
    card = litleXmlFields.cardType()
    card.number = "4100000000000000"
    card.expDate = "1210"
    card.type = 'VI'

    return card


@fixture()
def paypal_fixture():
    paypal = litleXmlFields.payPal()
    paypal.payerId = "1234"
    paypal.token = "1234"
    paypal.transactionId = '123456'

    return paypal


@fixture()
def applepay_fixture():
    applepay = litleXmlFields.applepayType()
    applepay.data = "4100000000000000"
    applepay.signature = "sign"
    applepay.version = '1'

    return applepay


@fixture()
def applepay_header_fixture():
    header = litleXmlFields.applepayHeaderType()
    header.applicationData = \
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    header.ephemeralPublicKey = \
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    header.publicKeyHash = \
        'e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855'
    header.transactionId = '1024'

    return header


@fixture()
def pos_fixture():
    pos = litleXmlFields.pos()
    pos.cardholderId = "pin"

    return pos


@fixture()
def capture_fixture():
    capture = litleXmlFields.capture()
    capture.litleTxnId = 123456000
    capture.amount = 110
    capture.payPalNotes = "Notes"

    return capture


@fixture()
def enhanced_data_fixture():
    enhanced = litleXmlFields.enhancedData()
    enhanced.customerReference = "Litle"
    enhanced.salesTax = 50
    enhanced.deliveryType = "TBD"

    return enhanced


@fixture()
def credit_fixture():
    credit = litleXmlFields.credit()
    credit.amount = 110
    credit.orderId = "12344"
    credit.orderSource = 'ecommerce'

    return credit


@fixture()
def credit_txn_fixture():
    credit = litleXmlFields.credit()
    credit.amount = 110
    credit.litleTxnId = "12345"
    credit.orderSource = 'ecommerce'

    return credit
