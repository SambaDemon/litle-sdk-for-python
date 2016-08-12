import exampleConfig
from litleSdkPython.litleOnlineRequest import litleOnlineRequest, litleXmlFields

config = exampleConfig.set_config()
card = exampleConfig.set_card()
contact = exampleConfig.set_contact()
void = litleXmlFields.void()

litleXml = litleOnlineRequest(config)

# Set the sale with card
sale = litleXmlFields.sale()
sale.orderId = "2"
sale.amount = 10010
sale.orderSource = "ecommerce"
sale.billToAddress = contact
sale.card = card

response = litleXml.sendRequest(sale)

print('\n')
print('Send sale with card request:')
exampleConfig.display_results(response)

# Void current sale
void.litleTxnId = response.litleTxnId
response = litleXml.sendRequest(void)

print('\n')
print('Void current sale request')
exampleConfig.display_results(response)

# Set the sale with token and clear card state first
sale.card = None
token = litleXmlFields.cardTokenType()
token.litleToken = "1234123412341234"
token.expDate = "0112"
token.cardValidationNum = "349"
token.type = "VI"

sale.token = token

response = litleXml.sendRequest(sale)

print('\n')
print('Send sale with token request')
exampleConfig.display_results(response)

# Void current sale
void.litleTxnId = response.litleTxnId
response = litleXml.sendRequest(void)

print('\n')
print('Void current sale request')
exampleConfig.display_results(response)

if response.response != "000":
    raise Exception("Incorrect response")
