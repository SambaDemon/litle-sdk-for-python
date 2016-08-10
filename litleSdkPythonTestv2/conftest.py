from pytest import fixture
from litleSdkPython.litleOnlineRequest import Configuration


@fixture(scope="class")
def config():
    config = Configuration()
    config.username = "username"
    config.password = "password"
    config.url = 'Sandbox'
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
    config.reportGroup = "Test Report Group"
    config.batchRequestFolder = "test/unit/"
    config.batchResponseFolder = "test/unit/"
    config.sftpUsername = "sftp"
    config.sftpPassword = "password"

    return config
