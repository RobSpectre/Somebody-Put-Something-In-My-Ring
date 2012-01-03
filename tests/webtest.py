import unittest
try:
    from app import app
except ImportError:
    import sys
    import os.path
    sys.path.append(os.path.abspath('.'))
    from app import app
from twiml import WebTest

class Test_Index(WebTest):
    def test_index(self):
        response = self.app.get("/")
        self.assertEqual("200 OK", response.status)
        self.assertFalse("Twilio.Device.setup(\"\")" in response.data, "No " \
                "token generated in page.")
