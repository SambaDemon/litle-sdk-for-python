import exampleConfig
from litleSdkPython.litleOnlineRequest import litleOnlineRequest, litleXmlFields


config = exampleConfig.set_config()
config.printXml = True
card = exampleConfig.set_card()
contact = exampleConfig.set_contact()

litleXml = litleOnlineRequest(config)

# TODO: Create plan
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

# TODO: Send subscription
# TODO: Update subscription with discount
# TODO: Send subscription with discount
# TODO: Cancel subscription

response = litleXml.sendRequest(plan)
