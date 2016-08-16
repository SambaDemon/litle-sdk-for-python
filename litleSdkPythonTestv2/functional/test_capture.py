import pytest
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestCapture:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleCapture(self, capture_fixture):
        capture = capture_fixture

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(capture)

        assert(response.message == "Approved")

    def testSimpleCaptureWithPartial(self, capture_fixture):
        capture = capture_fixture
        capture.partial = True

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(capture)

        assert(response.message == "Approved")

    def testComplexCapture(self, capture_fixture, enhanced_data_fixture):
        capture = capture_fixture
        enhanced = enhanced_data_fixture
        capture.enhancedData = enhanced
        capture.payPalOrderComplete = True

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(capture)

        assert(response.message == "Approved")
