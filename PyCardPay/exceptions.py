class PyCardPayException(Exception):
    """Base PyCardPay exception."""
    pass


class ParsingError(PyCardPayException):
    def __init__(self, msg, method=None, url=None, data=None, content=None):
        self.msg = msg
        self.method = method
        self.url = url
        self.data = data
        self.content = content
        super(ParsingError, self).__init__(msg)


class XMLParsingError(ParsingError):
    """Raised when lxml failed to parse xml from string"""
    pass


class JSONParsingError(ParsingError):
    """Raised when failed to parse json from string"""
    pass


class SignatureError(PyCardPayException):
    """Raised when signature doesn't match response"""
    pass


class HTTPError(PyCardPayException):
    """Raised when requests.Response.response_code contains value
    other than 2xx.
    """
    def __init__(self, msg, method=None, url=None, data=None, response=None):
        self.msg = msg
        self.method = method
        self.url = url
        self.data = data
        self.response = response
        super(HTTPError, self).__init__(msg)


class CommunicationError(PyCardPayException):
    """Raised when arbitrary requests exception occures"""
    def __init__(self, msg, exc):
        self.exc = exc
        self.msg = msg
        super(CommunicationError, self).__init__(exc)


class TransactionNotFound(PyCardPayException):
    pass
