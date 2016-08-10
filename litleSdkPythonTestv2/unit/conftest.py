from pytest import fixture


simple_extra_field = "<litleOnlineResponse version='8.13' response='0' message='Valid Format' \
                    xmlns='http://www.litle.com/schema'><captureGivenAuthResponse id='' \
                    reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId>\
                    <orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime>\
                    <message>Approved</message><authCode>83307</authCode></captureGivenAuthResponse>\
                    </litleOnlineResponse>"
simple_extra_field_embedded_extra_filed =  "<litleOnlineResponse version='8.13' response='0' message='Valid Format' \
                    xmlns='http://www.litle.com/schema'><captureGivenAuthResponse id='' \
                    reportGroup='DefaultReportGroup' customerId=''><litleTxnId>057484783403434000</litleTxnId>\
                    <orderId>12344</orderId><response>000</response><responseTime>2012-06-05T16:36:39</responseTime>\
                    <message>Approved</message><authCode><extraField>extra</extraField></authCode>\
                    </captureGivenAuthResponse></litleOnlineResponse>"


@fixture(params=simple_extra_field)
def simple_exf():
    return simple_extra_field
