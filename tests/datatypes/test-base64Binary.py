from pyxb.exceptions_ import *
import unittest, base64
import pyxb.binding.datatypes as xsd

b64data = u"""MIIDGTCCAoICCQCSNBowQENOqjANBgkqhkiG9w0BAQUFADCB0DELMAkGA1UEBhMC
WkExFTATBgNVBAgTDFdlc3Rlcm4gQ2FwZTESMBAGA1UEBxMJQ2FwZSBUb3duMR0w
GwYDVQQKExRWaXNpb25PU1MgKFB0eSkgTHRkLjEhMB8GA1UECxMYUmVzZWFyY2gg
YW5kIERldmVsb3BtZW50MSEwHwYDVQQDExh0ZXN0LXNwLnphLnZpc2lvbm9zcy5p
bnQxMTAvBgkqhkiG9w0BCQEWIm1pY2hhZWwudmR3ZXN0aHVpemVuQHZpc2lvbm9z
cy5jb20wHhcNMDkxMDA5MDk0MDI2WhcNMjkxMDA0MDk0MDI2WjCB0DELMAkGA1UE
BhMCWkExFTATBgNVBAgTDFdlc3Rlcm4gQ2FwZTESMBAGA1UEBxMJQ2FwZSBUb3du
MR0wGwYDVQQKExRWaXNpb25PU1MgKFB0eSkgTHRkLjEhMB8GA1UECxMYUmVzZWFy
Y2ggYW5kIERldmVsb3BtZW50MSEwHwYDVQQDExh0ZXN0LXNwLnphLnZpc2lvbm9z
cy5pbnQxMTAvBgkqhkiG9w0BCQEWIm1pY2hhZWwudmR3ZXN0aHVpemVuQHZpc2lv
bm9zcy5jb20wgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAK9TpyNf0yv+dRJd
qyVX6DgHKWsuIEx32fgiHMZJJoAZ+PaR8Da+sgJZlR3QPebVhHTBTzL13GxhH2xi
ubBij+yPEIbylLrXNZWs2J2xRqm9+uyYhhsoLBnI/whpuEHrbaQJ1KKGCQjYu82g
QmHsuPzFts9Z0BcvXn5rpb55n2oRAgMBAAEwDQYJKoZIhvcNAQEFBQADgYEAPWtx
t1aVW+iPbar9hSRJINhHvzfOtzINHUu8MCzak1T8uRZHUWXK+/LjpPV2yUXy9btr
trnT8w5eCgoGfXeqeQC6KhrDln3+Hi3KTNLEyWgBswtoS4XFkzZBklAqyNFoZgI9
+IEJMaLHchPOcQDzfXVC0veUsV2Rtj7ydY5Ajbw="""

binData = base64.b64decode(b64data)

expected = b64data.replace('\n', '').strip()


class Test_base64Binary (unittest.TestCase):
    def testFromLexicalSpace (self):
        self.assertEqual(xsd.base64Binary(b64data), binData)
        self.assertEqual(xsd.base64Binary(b64data.encode('utf8').decode('utf8')), binData)
        self.assertEqual(xsd.base64Binary(unicode(base64.b64encode(u'\x00'))), '\x00')

    def testValueSpace (self):
        self.assertEqual(xsd.base64Binary(binData), binData)
        self.assertEqual(base64.b64encode(xsd.base64Binary(binData)), expected)
        self.assertEqual(xsd.base64Binary('\x00'), '\x00')

    def testInvalid (self):
        self.assertRaises(BadTypeValueError, xsd.base64Binary, u"aacfgv")

if __name__ == '__main__':
    unittest.main()
