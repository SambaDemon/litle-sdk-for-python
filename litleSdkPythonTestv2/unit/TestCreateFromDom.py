# Copyright (c) 2011-2012 Litle & Co.
#
# Permission is hereby granted, free of charge, to any person
# obtaining a copy of this software and associated documentation
# files (the "Software"), to deal in the Software without
# restriction, including without limitation the rights to use,
# copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the
# Software is furnished to do so, subject to the following
# conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
# OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
# HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
# WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

from SetupTest import *


class TestCreateFromDom():

    def test_simple_extra_field(self, simple_extra_field):
        xml_object = litleXmlFields.CreateFromDocument(simple_extra_field)
        self.assertEqual("Approved", xml_object.transactionResponse.message)

    def test_simple_extra_field_embedded_extra_field(self, simple_extra_field_embedded_extra_field):
        xml_object = litleXmlFields.CreateFromDocument(simple_extra_field_embedded_extra_field)
        self.assertEqual("Approved", xml_object.transactionResponse.message)

    def test_simple_EmbeddedField(self):
        test = ("""<litleOnlineResponse version='10.1' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'>
                <authorizationResponse id='' reportGroup='Default Report Group' customerId=''>
                <litleTxnId>100000000000000011</litleTxnId>
                <orderId>1</orderId>
                <response>000</response>
                <responseTime>2016-07-27T07:38:00</responseTime>
                <message>Approved</message>
                <authCode>11111 </authCode>
                <fraudResult>
                <avsResult>01</avsResult>
                <cardValidationResult>M</cardValidationResult>
                </fraudResult>
                </authorizationResponse>
                </litleOnlineResponse>""")
        xml_text = ("""<litleOnlineResponse version='8.13' response='0' message='Valid Format' xmlns='http://www.litle.com/schema'>
                    <authorizationResponse id='' reportGroup='DefaultReportGroup'customerId=''>
                    <litleTxnId>057484783403434000</litleTxnId>
                    <orderId>12344</orderId>
                    <response>000</response>
                    <responseTime>2012-06-05T16:36:39</responseTime>
                    <message>Approved</message>
                    <tokenResponse><litleToken>4242424242424242</litleToken><tokenResponseCode>111</tokenResponseCode>
                    <tokenMessage>Message</tokenMessage><bin>bin</bin></tokenResponse>
                    </authorizationResponse>
                    </litleOnlineResponse>""")
        xml_object = litleXmlFields.CreateFromDocument(xml_text)
        self.assertEqual("bin", xml_object.transactionResponse.tokenResponse.bin)
        self.assertEqual("Message", xml_object.transactionResponse.tokenResponse.tokenMessage)

    def test_simple_ExtraEmbeddedField(self):
        xml_text = "<litleOnlineResponse version='8.13' response='0' message='Valid Format' \
        xmlns='http://www.litle.com/schema'><authorizationResponse id='' reportGroup='DefaultReportGroup' \
        customerId=''><litleTxnId>057484783403434000</litleTxnId><orderId>12344</orderId><response>000</response>\
        <responseTime>2012-06-05T16:36:39</responseTime><message>Approved</message><tokenResponse>\
        <litleToken>4242424242424242</litleToken><tokenResponseCode>111</tokenResponseCode>\
        <tokenMessage>Message</tokenMessage><bin>bin</bin><extra>extra</extra></tokenResponse></authorizationResponse>\
        </litleOnlineResponse>"
        xml_object = litleXmlFields.CreateFromDocument(xml_text)
        self.assertEqual("bin", xml_object.transactionResponse.tokenResponse.bin)
        self.assertEqual("Message", xml_object.transactionResponse.tokenResponse.tokenMessage)
