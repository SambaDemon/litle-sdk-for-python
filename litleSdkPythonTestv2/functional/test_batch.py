import os
import pytest
from litleSdkPython.litleBatchRequest import litleBatchFileRequest
from litleSdkPython.litleBatchResponse import litleBatchFileResponse
from litleSdkPython import litleXmlFields


class TestBatch:

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setup(self, config):
        self.config = config

    def testSendToLitleSFTP_WithPreviouslyCreatedFile(self):
        import ipdb; ipdb.set_trace() # DEBUG
        requestFileName = "litleSdk-testBatchFile-testSendToLitleSFTP_WithPreviouslyCreatedFile.xml" # noqa
        request = litleBatchFileRequest(requestFileName, config=self.config)
        requestFile = request.requestFile.name
        assert(os.path.exists(requestFile) == True)
        configFromFile = request.config
        assert(configFromFile.batchHost == 'localhost')
        assert(configFromFile.batchPort, '2104')
        requestDir = configFromFile.batchRequestFolder
        responseDir = configFromFile.batchResponseFolder
        self.prepareTestRequest(request)
        request.prepareForDelivery()
        assert(os.path.exists(requestFile) == True)
        assert(os.path.getsize(requestFile) > 0)
        request2 = litleBatchFileRequest(requestFileName)
        response = request2.sendRequestSFTP(True)
        self.assertPythonApi(request2, response)
        self.assertGeneratedFiles(
            requestDir, responseDir, requestFileName, request2)

    def assertPythonApi(self, request, response):
        assert(response is not None)
        assert(response.litleResponse.litleSessionId is not None)
        assert(response.litleResponse.response == '0')
        assert(response.litleResponse.message == 'Valid Format')
        assert(response.litleResponse.version == '9.3')

        batchResponse = response.getNextBatchResponse()
        assert(response is not None)
        assert(batchResponse.batchResponse.litleBatchId is not None)
        assert(batchResponse.batchResponse.merchantId == self.merchantId)

        saleResponse = batchResponse.getNextTransaction()
        assert(saleResponse.response == '000')
        assert(saleResponse.message == 'Approved')
        assert(saleResponse.litleTxnId is not None)
        assert(saleResponse.orderId == 'orderId11')
        assert(saleResponse.reportGroup == 'reportGroup11')

    def prepareTestRequest(self, request):
        batchRequest = request.createBatch()
        sale = litleXmlFields.sale()
        sale.reportGroup = 'Test Report Group'
        sale.orderId = 'orderId11'
        sale.amount = 1099
        sale.orderSource = 'ecommerce'

        card = litleXmlFields.cardType()
        card.type = 'VI'
        card.number = "4457010000000009"
        card.expDate = "0114"
        sale.card = card

        batchRequest.addTransaction(sale)

    def assertGeneratedFiles(
            self, requestDir, responseDir, requestFileName, request):
        requestPath = requestDir + '/' + requestFileName
        responsePath = responseDir + '/' + requestFileName
        fRequest = os.path.abspath(request.requestFile.name)
        fResponse = os.path.abspath(request.responseFile.name)

        assert(requestPath == fRequest)
        assert(responsePath == fResponse)
        assert(os.path.exists(fRequest) == True)
        assert(os.path.exists(fResponse) == True)
        assert(os.path.getsize(fRequest) > 0)
        assert(os.path.getsize(fResponse) > 0)

        responseFromFile = litleBatchFileResponse(fResponse)
        self.assertPythonApi(request, responseFromFile)
