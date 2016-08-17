import pytest
from litleSdkPython.litleOnlineRequest import litleOnlineRequest


class TestForceCapture:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSimpleForceCaptureWithCard(
            self, force_capture_fixture, card_fixture):
        forcecapture = force_capture_fixture
        card = card_fixture
        forcecapture.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(forcecapture)
        assert(response.message == "Approved")

    def testSimpleForceCaptureWithToken(
            self, force_capture_fixture, card_token_fixture):
        forcecapture = force_capture_fixture
        token = card_token_fixture
        forcecapture.token = token

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(forcecapture)
        assert(response.message == "Approved")

    def testSimpleForceCaptureWithSecondaryAmount(
            self, force_capture_fixture, card_fixture):
        forcecapture = force_capture_fixture
        forcecapture.secondaryAmount = 10
        card = card_fixture
        forcecapture.card = card

        litleXml = litleOnlineRequest(self.config)
        response = litleXml.sendRequest(forcecapture)
        assert(response.message == "Approved")
