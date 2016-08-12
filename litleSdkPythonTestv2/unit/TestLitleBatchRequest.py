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
import pytest
from mock import *
from litleSdkPython.litleBatchRequest import (litleBatchFileRequest,
                                              TransactionCode)
from litleSdkPython import litleXmlFields


class TestLitleBatchRequest():

    @classmethod
    @pytest.fixture(scope="class", autouse=True)
    def setUp(self, config):
        config = config
        config.username = "PHXMLTEST"
        config.password = "password"
        config.version = "9.3"
        config.maxAllowedTransactionsPerFile = "6"
        config.maxTransactionsPerBatch = "4"
        config.batchHost = "localhost"
        config.batchPort = "2104"
        config.batchTcpTimeout = "10000"
        config.batchUseSSL = "false"
        config.merchantId = "101"
        config.proxyHost = ""
        config.proxyPort = ""
        config.reportGroup = "test"
        config.batchRequestFolder = "test/unit/"
        config.batchResponseFolder = "test/unit/"
        config.sftpUsername = "sftp"
        config.sftpPassword = "password"
        self.litleBatchFileRequest = litleBatchFileRequest("testFile.xml",
                                                           config)

    # Tests for litleBatchFileRequest

    def testInit(self):
        assert(self.litleBatchFileRequest.config.username == 'PHXMLTEST')
        assert(self.litleBatchFileRequest.config.password, 'password')
        assert(self.litleBatchFileRequest.config.version, '9.3')
        assert(self.litleBatchFileRequest.config.maxAllowedTransactionsPerFile == '6')
        assert(
            self.litleBatchFileRequest.config.maxTransactionsPerBatch == '4')
        assert(
            self.litleBatchFileRequest.config.batchHost == 'localhost')
        assert(self.litleBatchFileRequest.config.batchPort == '2104')
        assert(
            self.litleBatchFileRequest.config.batchTcpTimeout == '10000')
        assert(self.litleBatchFileRequest.config.batchUseSSL == 'false')
        assert(self.litleBatchFileRequest.config.merchantId == '101')
        assert(self.litleBatchFileRequest.config.proxyHost == '')
        assert(self.litleBatchFileRequest.config.proxyPort == '')
        assert(self.litleBatchFileRequest.config.reportGroup == 'test')
        assert(self.litleBatchFileRequest.config.batchRequestFolder == 'test/unit/')
        assert(
            self.litleBatchFileRequest.config.batchResponseFolder ==
            'test/unit/')
        assert(self.litleBatchFileRequest.config.sftpUsername == 'sftp')
        assert(self.litleBatchFileRequest.config.sftpPassword == 'password')

    def testCreateBatchAndGetNumberOfBatches(self):
        assert(self.litleBatchFileRequest.getNumberOfBatches() == 0)

        testBatch = self.litleBatchFileRequest.createBatch()
        assert(testBatch is not None)

        assert(self.litleBatchFileRequest.getNumberOfBatches() == 1)

    def testGetNumberOfTransactionInFile(self):
        assert(self.litleBatchFileRequest.getNumberOfTransactionInFile() == 0)

        testBatch = self.litleBatchFileRequest.createBatch()
        testBatch.numOfTxn = 2
        testBatch2 = self.litleBatchFileRequest.createBatch()
        testBatch2.numOfTxn = 3

        assert(self.litleBatchFileRequest.getNumberOfTransactionInFile() == 5)

    def testIsEmpty(self):
        # assert(self.litleBatchFileRequest.isEmpty())

        testBatch = self.litleBatchFileRequest.createBatch()
        testBatch.numOfTxn = 5
        assert(not self.litleBatchFileRequest.isEmpty())

    def testFileIsFull(self, config):
        config = config
        config.username = "PHXMLTEST"
        config.password = "password"
        config.version = "8.25"
        config.maxAllowedTransactionsPerFile = "4"
        config.maxTransactionsPerBatch = "4"
        config.batchHost = "localhost"
        config.batchPort = "2104"
        config.batchTcpTimeout = "10000"
        config.batchUseSSL = "false"
        config.merchantId = "101"
        config.proxyHost = ""
        config.proxyPort = ""
        config.reportGroup = "test"
        config.batchRequestFolder = "test/unit/"
        config.batchResponseFolder = "test/unit/"
        config.sftpUsername = "sftp"
        config.sftpPassword = "password"

        self.litleBatchFileRequest = litleBatchFileRequest(
            "testFile.xml", config)

        assert(not self.litleBatchFileRequest.isFull())

        testBatch = self.litleBatchFileRequest.createBatch()
        testBatch.numOfTxn = 4

        assert(self.litleBatchFileRequest.isFull())

    # Tests for litleBatchRequest
    def testIsFull(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        assert(not batchRequest.isFull())
        batchRequest.numOfTxn = 4
        assert(batchRequest.isFull())

    def testVerifyFileThresholds(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        batchRequest.numOfTxn = 3
        assert(batchRequest.verifyFileThresholds() == TransactionCode.SUCCESS)
        batchRequest.numOfTxn = 4
        assert(batchRequest.verifyFileThresholds() == TransactionCode.BATCHFULL)

        batchRequest2 = self.litleBatchFileRequest.createBatch()
        batchRequest2.numOfTxn = 2

        assert(batchRequest.verifyFileThresholds() == TransactionCode.FILEFULL)

    def testAddTransaction(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')
        assert(batchRequest.addTransaction(createTestSale(100, '100')) ==
               TransactionCode.SUCCESS)
        assert(batchRequest.addTransaction(createTestSale(100, '100')) ==
               TransactionCode.SUCCESS)
        assert(batchRequest.addTransaction(createTestSale(100, '100')) ==
               TransactionCode.SUCCESS)
        assert(batchRequest.addTransaction(createTestSale(100, '100')) ==
               TransactionCode.BATCHFULL)
        batchFullException = False
        try:
            batchRequest.addTransaction(createTestSale(100, '100'))
        except:
            batchFullException = True

        assert(batchFullException)

        batchRequest2 = self.litleBatchFileRequest.createBatch()
        assert(batchRequest2.addTransaction(createTestSale(100, '100')) ==
               TransactionCode.SUCCESS)
        assert(batchRequest2.addTransaction(createTestSale(100, '100')) ==
               TransactionCode.FILEFULL)

        fileFullException = False
        try:
            batchRequest2.addTransaction(createTestSale(100, '100'))
        except:
            fileFullException = True

        assert(fileFullException)

    def testOverrideMerchantId(self):
        batchRequest = self.litleBatchFileRequest.createBatch('101')
        assert(batchRequest._batchRequest.merchantId == '101')

    def testAddSale(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        sale = litleXmlFields.sale()
        sale.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(sale)
        assert(batchRequest._batchRequest.saleAmount == 25)
        assert(batchRequest._batchRequest.numSales == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddAuth(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        auth = litleXmlFields.authorization()
        auth.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(auth)
        assert(batchRequest._batchRequest.authAmount == 25)
        assert(batchRequest._batchRequest.numAuths == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddCredit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        credit = litleXmlFields.credit()
        credit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(credit)
        assert(batchRequest._batchRequest.creditAmount == 25)
        assert(batchRequest._batchRequest.numCredits == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddRegisterTokenRequest(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        registerTokenRequest = litleXmlFields.registerTokenRequest()
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(registerTokenRequest)
        assert(batchRequest._batchRequest.numTokenRegistrations == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddCaptureGivenAuth(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        captureGivenAuth = litleXmlFields.captureGivenAuth()
        captureGivenAuth.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(captureGivenAuth)
        assert(batchRequest._batchRequest.captureGivenAuthAmount == 25)
        assert(batchRequest._batchRequest.numCaptureGivenAuths == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddForceCapture(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        forceCapture = litleXmlFields.forceCapture()
        forceCapture.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(forceCapture)
        assert(batchRequest._batchRequest.forceCaptureAmount == 25)
        assert(batchRequest._batchRequest.numForceCaptures == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddAuthReversal(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        authReversal = litleXmlFields.authReversal()
        authReversal.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(authReversal)
        assert(batchRequest._batchRequest.authReversalAmount == 25)
        assert(batchRequest._batchRequest.numAuthReversals == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddCapture(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        capture = litleXmlFields.capture()
        capture.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(capture)
        assert(batchRequest._batchRequest.captureAmount == 25)
        assert(batchRequest._batchRequest.numCaptures == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddEcheckVerification(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        echeckVerification = litleXmlFields.echeckVerification()
        echeckVerification.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(echeckVerification)
        assert(
            batchRequest._batchRequest.echeckVerificationAmount == 25)
        assert(batchRequest._batchRequest.numEcheckVerification == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddEcheckCredit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        echeckCredit = litleXmlFields.echeckCredit()
        echeckCredit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(echeckCredit)
        assert(batchRequest._batchRequest.echeckCreditAmount == 25)
        assert(batchRequest._batchRequest.numEcheckCredit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddEcheckRedeposit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        echeckRedeposit = litleXmlFields.echeckRedeposit()
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(echeckRedeposit)
        assert(batchRequest._batchRequest.numEcheckRedeposit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddEcheckSale(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        echeckSale = litleXmlFields.echeckSale()
        echeckSale.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(echeckSale)
        assert(batchRequest._batchRequest.echeckSalesAmount == 25)
        assert(batchRequest._batchRequest.numEcheckSales == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddUpdateCardValidationNumOnToken(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        updateCardValidationNumOnToken = litleXmlFields.updateCardValidationNumOnToken()
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(updateCardValidationNumOnToken)
        assert(
            batchRequest._batchRequest.numUpdateCardValidationNumOnTokens == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddAccountUpdate(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        accountUpdate = litleXmlFields.accountUpdate()
        batchRequest._batchRequest.numAccountUpdates = 1
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(accountUpdate)
        assert(batchRequest._batchRequest.numAccountUpdates == 2)
        assert(batchRequest.numOfTxn == 1)

    def testAddAUBlock_AU_side(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        accountUpdate = litleXmlFields.accountUpdate()
        batchRequest._batchRequest.numAccountUpdates = 1
        batchRequest.numOfTxn = 1
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(accountUpdate)
        assert(batchRequest._batchRequest.numAccountUpdates == 2)
        assert(batchRequest.numOfTxn == 2)

        sale = litleXmlFields.sale()
        sale.amount = 5

        exception = None
        try:
            batchRequest.addTransaction(sale)
        except Exception as e:
            exception = e
        assert(exception is not None)

    def testAddAUBlock_Sale_side(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        sale = litleXmlFields.sale()
        sale.amount = 5

        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')
        batchRequest.addTransaction(sale)
        assert(batchRequest._batchRequest.numSales == 1)
        assert(batchRequest._batchRequest.saleAmount == 5)
        assert(batchRequest.numOfTxn == 1)

        accountUpdate = litleXmlFields.accountUpdate()

        exception = None
        try:
            batchRequest.addTransaction(accountUpdate)
        except Exception as e:
            exception = e
        assert(exception is not None)

    def testAddSubmerchantCredit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        submerchantCredit = litleXmlFields.submerchantCredit()
        submerchantCredit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(submerchantCredit)
        assert(batchRequest._batchRequest.submerchantCreditAmount == 25)
        assert(batchRequest._batchRequest.numSubmerchantCredit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddSubmerchantDebit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        submerchantDebit = litleXmlFields.submerchantDebit()
        submerchantDebit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(submerchantDebit)
        assert(batchRequest._batchRequest.submerchantDebitAmount == 25)
        assert(batchRequest._batchRequest.numSubmerchantDebit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddPayFacCredit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        payFacCredit = litleXmlFields.payFacCredit()
        payFacCredit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(payFacCredit)
        assert(batchRequest._batchRequest.payFacCreditAmount == 25)
        assert(batchRequest._batchRequest.numPayFacCredit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddPayFacDebit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        payFacDebit = litleXmlFields.payFacDebit()
        payFacDebit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(payFacDebit)
        assert(batchRequest._batchRequest.payFacDebitAmount == 25)
        assert(batchRequest._batchRequest.numPayFacDebit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddReserveCredit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        reserveCredit = litleXmlFields.reserveCredit()
        reserveCredit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(reserveCredit)
        assert(batchRequest._batchRequest.reserveCreditAmount == 25)
        assert(batchRequest._batchRequest.numReserveCredit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddReserveDebit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        reserveDebit = litleXmlFields.reserveDebit()
        reserveDebit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(reserveDebit)
        assert(batchRequest._batchRequest.reserveDebitAmount == 25)
        assert(batchRequest._batchRequest.numReserveDebit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddVendorCredit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        vendorCredit = litleXmlFields.vendorCredit()
        vendorCredit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(vendorCredit)
        assert(batchRequest._batchRequest.vendorCreditAmount == 25)
        assert(batchRequest._batchRequest.numVendorCredit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddVendorDebit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        vendorDebit = litleXmlFields.vendorDebit()
        vendorDebit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(vendorDebit)
        assert(batchRequest._batchRequest.vendorDebitAmount == 25)
        assert(batchRequest._batchRequest.numVendorDebit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddPhysicalCheckCredit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        physicalCheckCredit = litleXmlFields.physicalCheckCredit()
        physicalCheckCredit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(physicalCheckCredit)
        assert(batchRequest._batchRequest.physicalCheckCreditAmount == 25)
        assert(batchRequest._batchRequest.numPhysicalCheckCredit == 1)
        assert(batchRequest.numOfTxn == 1)

    def testAddPhysicalCheckDebit(self):
        batchRequest = self.litleBatchFileRequest.createBatch()
        physicalCheckDebit = litleXmlFields.physicalCheckDebit()
        physicalCheckDebit.amount = 25
        self.litleBatchFileRequest.tnxToXml = MagicMock(return_value='')

        batchRequest.addTransaction(physicalCheckDebit)
        assert(batchRequest._batchRequest.physicalCheckDebitAmount == 25)
        assert(batchRequest._batchRequest.numPhysicalCheckDebit == 1)
        assert(batchRequest.numOfTxn == 1)


def createTestSale(amount, orderId):
    sale = litleXmlFields.sale()
    sale.amount = amount
    sale.orderId = orderId
    sale.orderSource = 'ecommerce'
    card = litleXmlFields.cardType()
    card.type = 'VI'
    card.number = "4100000000000001"
    card.expDate = "1210"
    sale.card = card
    sale.reportGroup = 'test'
    return sale
