import pytest
from litleSdkPython import litleXmlFields
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestAuthReversal:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleAuthReversal(self):
        reversal = litleXmlFields.authReversal()
        reversal.litleTxnId = 12345678000
        reversal.amount = 106
        reversal.payPalNotes = "Notes"

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(reversal)

        assert("Approved" == response.message)
