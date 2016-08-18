import pyxb.binding.datatypes as pdt
import exampleConfig
from litleSdkPython.litleOnlineRequest import litleOnlineRequest, litleXmlFields


config = exampleConfig.set_config()
config.printXml = True
card = exampleConfig.set_card()

litleXml = litleOnlineRequest(config)

# Create plan
plan = litleXmlFields.createPlan()
plan.planCode = '3_Year_Monthly'
plan.name = '3Year_Monthly'
plan.description = '3 Year, monthly Payments, 1 month trial'
plan.intervalType = 'MONTHLY'
plan.amount = 25000
plan.numberOfPayments = 36
plan.trialNumberOfIntervals = 1
plan.trialIntervalType = 'MONTH'
plan.active = True

response = litleXml.sendRequest(plan)

# Send subscription as a part of an auth
auth = litleXmlFields.authorization()
auth.orderId = '1'
auth.amount = 1
auth.orderSource = 'ecommerce'
auth.card = card

recurring = litleXmlFields.recurringRequestType()
subscription = litleXmlFields.recurringSubscriptionType()
subscription.planCode = '3_Year_Monthly'
subscription.numberOfPayments = 36
subscription.startDate = pdt.date(2016, 10, 20)
subscription.amount = 1000
recurring.subscription = subscription

auth.recurringRequest = recurring

response = litleXml.sendRequest(auth)

# Update subscription with discount
update = litleXmlFields.updateSubscription()
update.subscriptionId = response.recurringResponse.subscriptionId
discount = litleXmlFields.createDiscountType()
discount.discountCode = 'SUMMERSALE2016'
discount.name = 'Discount Name'
discount.amount = 1
discount.startDate = pdt.date(2016, 10, 20)
discount.endDate = pdt.date(2016, 10, 20)
update.createDiscount = [discount, ]

response = litleXml.sendRequest(update)

# Send subscription with discount
auth.orderId = '2'
discount.discountCode = 'AUTUMNSALE2016'
auth.recurringRequest.subscription.createDiscount = [discount, ]

response = litleXml.sendRequest(auth)

# Cancel subscription
cancel = litleXmlFields.cancelSubscription()
cancel.subscriptionId = response.recurringResponse.subscriptionId

response = litleXml.sendRequest(cancel)
