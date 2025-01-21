import logging
from ib_insync import *

class CustomFilter(logging.Filter):
    """Filter to suppress common IB API error messages."""
    def __init__(self):
        super().__init__()
        self.ignore_messages = [
            "Unknown contract",
            "Es wurde keine Wertpapierdefinition zu der Anfrage gefunden",
            "No security definition has been found for the request",
            "Unable to parse field"
        ]

    def filter(self, record):
        return not any(ignore_msg in record.getMessage() for ignore_msg in self.ignore_messages)

class CustomIB(IB):
    """Custom IB class with error filtering and improved logging."""
    def __init__(self):
        super().__init__()
        self._configure_logging()
        self.RequestTimeout = 30  # Increase timeout for requests
        
    def _configure_logging(self):
        """Configure logging with custom filter."""
        logger = logging.getLogger()
        logger.setLevel(logging.ERROR)
        
        # Remove existing handlers and add our custom one
        for handler in logger.handlers[:]:
            logger.removeHandler(handler)
        
        handler = logging.StreamHandler()
        handler.addFilter(CustomFilter())
        logger.addHandler(handler)

    def error(self, reqId, errorCode, errorString, contract=None):
        """Filter out common non-critical error codes."""
        ignore_codes = {200, 354, 2104, 2106, 2158, 320}  # Added 320 for contract parsing issues
        if errorCode in ignore_codes:
            return
        super().error(reqId, errorCode, errorString, contract)
    
    def connect(self, host='127.0.0.1', port=7497, clientId=1, timeout=20):
        """Enhanced connect method with retry logic."""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                if not self.isConnected():
                    super().connect(host, port, clientId, readonly=False, timeout=timeout)
                    print(f'IB Connection established with clientId={clientId}')
                return True
            except Exception as e:
                if attempt == max_retries - 1:  # Last attempt
                    print(f'Failed to connect to IB after {max_retries} attempts: {str(e)}')
                    return False
                print(f'Connection attempt {attempt + 1} failed, retrying...')
                self.sleep(1)
        return False

def create_ib_connection(port=7497, clientid=10):
    """
    Create and return a CustomIB connection.
    
    Args:
        port: IB Gateway/TWS port (default: 7497)
        clientid: Client ID for the connection (default: 10)
    
    Returns:
        CustomIB instance if connection successful, None otherwise
    """
    ib = CustomIB()
    if ib.connect('127.0.0.1', port, clientId=clientid, timeout=20):
        return ib
    return None
