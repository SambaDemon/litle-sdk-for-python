import exampleConfig
from litleSdkPython.litleOnlineRequest import litleOnlineRequest, litleXmlFields

config = exampleConfig.set_config()
card = exampleConfig.set_card()

# Set Authorization
auth = litleXmlFields.authorization()
auth.orderId = '1'
auth.amount = 1
auth.orderSource = 'ecommerce'
auth.card = card

litleXml = litleOnlineRequest(config)
response = litleXml.sendRequest(auth)

# Display results
print('\n')
print('Check that customer has' +
      ' sufficient funds to purchase the goods or services:')
exampleConfig.display_results(response)

# Set Authorization Reversal
auth_reversal = litleXmlFields.authReversal()
auth_reversal.amount = 1
auth_reversal.litleTxnId = response.litleTxnId
response = litleXml.sendRequest(auth_reversal)

# Display results
print('\n')
print('Eliminate previously frozen amount on used authorization:')
exampleConfig.display_results(response)

if response.response != "000":
    raise Exception("Incorrect Response")
