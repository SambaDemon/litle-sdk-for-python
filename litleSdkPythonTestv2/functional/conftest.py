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

    return credit


@fixture()
def echeck_credit_txn_fixture():
    echeckCredit = litleXmlFields.echeckCredit()
    echeckCredit.amount = 12
    echeckCredit.litleTxnId = 123456789101112

    return echeckCredit


@fixture()
def echeck_credit_fixture():
    echeckCredit = litleXmlFields.echeckCredit()
    echeckCredit.amount = 12
    echeckCredit.orderId = "12345"
    echeckCredit.orderSource = 'ecommerce'

    return echeckCredit


@fixture()
def echeck_fixture():
    echeck = litleXmlFields.echeck()
    echeck.accType = 'Checking'
    echeck.accNum = "1234567890"
    echeck.routingNum = "123456789"
    echeck.checkNum = "123455"

    return echeck


@fixture()
def contact_fixture():
    billToAddress = litleXmlFields.contact()
    billToAddress.name = "Bob"
    billToAddress.City = "Lowell"
    billToAddress.State = "MA"
    billToAddress.email = "litle.com"

    return billToAddress


@fixture()
def echeck_token_fixture():
    token = litleXmlFields.echeckToken()
    token.accType = 'Checking'
    token.litleToken = "1234565789012"
    token.routingNum = "123456789"
    token.checkNum = "123455"

    return token


@fixture()
def echeck_sale_fixture():
    echecksale = litleXmlFields.echeckSale()
    echecksale.amount = 123456
    echecksale.orderId = "12345"
    echecksale.orderSource = 'ecommerce'

    return echecksale


@fixture()
def echeck_sale_txn_fixture():
    echecksale = litleXmlFields.echeckSale()
    echecksale.litleTxnId = 123456789101112
    echecksale.amount = 12

    return echecksale


@fixture()
def echeck_verfication_fixture():
    echeckverification = litleXmlFields.echeckVerification()
    echeckverification.amount = 123456
    echeckverification.orderId = '12345'
    echeckverification.orderSource = 'ecommerce'

    return echeckverification


@fixture()
def force_capture_fixture():
    forcecapture = litleXmlFields.forceCapture()
    forcecapture.amount = 106
    forcecapture.orderId = '12344'
    forcecapture.orderSource = 'ecommerce'

    return forcecapture


@fixture()
def card_token_fixture():
    token = litleXmlFields.cardTokenType()
    token.type = 'VI'
    token.expDate = "1210"
    token.litleToken = "123456789101112"
    token.cardValidationNum = "555"

    return token


@fixture()
def sale_fixture():
    sale = litleXmlFields.sale()
    sale.litleTxnId = 123456
    sale.amount = 106
    sale.orderId = '12344'
    sale.orderSource = 'ecommerce'

    return sale


@fixture()
def register_token_fixture():
    token = litleXmlFields.registerTokenRequest()
    token.orderId = '12344'

    return token


@fixture()
def echeck_for_token_fixture():
    echeck = litleXmlFields.echeckForTokenType()
    echeck.accNum = "12344565"
    echeck.routingNum = "123476545"

    return echeck
