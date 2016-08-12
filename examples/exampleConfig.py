from litleSdkPython.litleOnlineRequest import Configuration, litleXmlFields


def set_config():
    '''
    If you want to display request and response body
    then set config.printXml = True
    '''
    config = Configuration()
    config.username = "jenkins"
    config.password = "certpass"
    config.merchantId = "0180"
    config.url = "Sandbox"
    config.proxy = "iwp1.lowell.litle.com:8080"

    return config


def set_card():
    card = litleXmlFields.cardType()
    card.number = "4457010000000009"
    card.expDate = "0112"
    card.cardValidationNum = "349"
    card.type = "VI"

    return card


def set_contact():
    contact = litleXmlFields.contact()
    contact.name = "John Smith"
    contact.addressLine1 = "1 Main St."
    contact.city = "Burlington"
    contact.state = "MA"
    contact.zip = "01803-3747"
    contact.country = "USA"

    return contact


def display_results(response):
    print("Response: " + response.response)
    print("Message: " + response.message)
    print("LitleTransaction ID: " + str(response.litleTxnId))
