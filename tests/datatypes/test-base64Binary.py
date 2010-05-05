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
    def testFromLexical (self):
        t1 = xsd.base64Binary(b64data)
        self.assertEqual(t1, binData)
        self.assertEqual(len(t1), t1.XsdValueLength(t1))
        t2 = xsd.base64Binary(b64data.encode('utf8').decode('utf8'))
        self.assertEqual(t2, binData)
        self.assertEqual(len(t2), t2.XsdValueLength(t2))
        t3 = xsd.base64Binary(unicode(base64.b64encode(u'\x00')))
        self.assertEqual(t3, '\x00')
        self.assertEqual(len(t3), t3.XsdValueLength(t3))

    def testFromValue (self):
        t1 = xsd.base64Binary(binData)
        self.assertEqual(t1, binData)
        self.assertEqual(base64.b64encode(t1), expected)
        self.assertEqual(len(t1), t1.XsdValueLength(t1))
        t2 = xsd.base64Binary('\x00')
        self.assertEqual(t2, '\x00')
        self.assertEqual(len(t2), t2.XsdValueLength(t2))

    def testWhitespace (self):
        b64_1 = unicode(b64data.replace('\n', '').replace('\t', '').replace(' ', ''))
        expected = b64_1
        b64_2 = unicode('\n'.join([x for x in b64_1]))
        b64_3_ = b64_1[:]
        b64_3 = u''
        i = 0
        while len(b64_3_) > 0:
            i += 1
            take = min(len(b64_3_), i % 10)
            b64_3 += b64_3_[0:take]
            b64_3 += '\n'
            b64_3_ = b64_3_[take:]
        t1 = xsd.base64Binary(b64_1)
        self.assertEqual(t1, binData)
        self.assertEqual(t1.XsdLiteral(t1), expected)
        t2 = xsd.base64Binary(b64_2)
        self.assertEqual(t2, binData)
        self.assertEqual(t2.XsdLiteral(t2), expected)
        t3 = xsd.base64Binary(b64_3)
        self.assertEqual(t3, binData)
        self.assertEqual(t3.XsdLiteral(t3), expected)

        self.assertEqual(len(t1), t1.XsdValueLength(t1))
        self.assertEqual(len(t2), t2.XsdValueLength(t2))
        self.assertEqual(len(t3), t3.XsdValueLength(t3))

    def testInvalidPlainText (self):
        self.assertRaises(BadTypeValueError, xsd.base64Binary, u"aacfgv")

        t1 = xsd.base64Binary("aacfgv")
        self.assertEquals(t1, "aacfgv")
        self.assertEquals(t1.XsdLiteral(t1), u"YWFjZmd2")
        self.assertEquals(len(t1), t1.XsdValueLength(t1))

        t1 = xsd.base64Binary(u"YWFjZmd2")
        self.assertEquals(t1, "aacfgv")
        self.assertEquals(t1.XsdLiteral(t1), u"YWFjZmd2")
        self.assertEquals(len(t1), t1.XsdValueLength(t1))

    def testRfc4648Vectors (self):
        i1 = ""
        e1 = u""
        t1 = xsd.base64Binary(i1)
        self.assertEqual(t1, i1)
        self.assertEqual(len(t1), len(i1))
        self.assertEqual(t1.XsdLiteral(t1), e1)
        t1 = xsd.base64Binary(e1)
        self.assertEqual(t1, i1)
        self.assertEqual(len(t1), len(i1))
        self.assertEqual(t1.XsdLiteral(t1), e1)

        i2 = "f"
        e2 = u"Zg=="
        t2 = xsd.base64Binary(i2)
        self.assertEqual(t2, i2)
        self.assertEqual(len(t2), len(i2))
        self.assertEqual(t2.XsdLiteral(t2), e2)
        t2 = xsd.base64Binary(e2)
        self.assertEqual(t2, i2)
        self.assertEqual(len(t2), len(i2))
        self.assertEqual(t2.XsdLiteral(t2), e2)

        i3 = "fo"
        e3 = u"Zm8="
        t3 = xsd.base64Binary(i3)
        self.assertEqual(t3, i3)
        self.assertEqual(len(t3), len(i3))
        self.assertEqual(t3.XsdLiteral(t3), e3)
        t3 = xsd.base64Binary(e3)
        self.assertEqual(t3, i3)
        self.assertEqual(len(t3), len(i3))
        self.assertEqual(t3.XsdLiteral(t3), e3)

        i4 = "foo"
        e4 = u"Zm9v"
        t4 = xsd.base64Binary(i4)
        self.assertEqual(t4, i4)
        self.assertEqual(len(t4), len(i4))
        self.assertEqual(t4.XsdLiteral(t4), e4)
        t4 = xsd.base64Binary(e4)
        self.assertEqual(t4, i4)
        self.assertEqual(len(t4), len(i4))
        self.assertEqual(t4.XsdLiteral(t4), e4)

        i5 = "foob"
        e5 = u"Zm9vYg=="
        t5 = xsd.base64Binary(i5)
        self.assertEqual(t5, i5)
        self.assertEqual(len(t5), len(i5))
        self.assertEqual(t5.XsdLiteral(t5), e5)
        t5 = xsd.base64Binary(e5)
        self.assertEqual(t5, i5)
        self.assertEqual(len(t5), len(i5))
        self.assertEqual(t5.XsdLiteral(t5), e5)

        i6 = "fooba"
        e6 = u"Zm9vYmE="
        t6 = xsd.base64Binary(i6)
        self.assertEqual(t6, i6)
        self.assertEqual(len(t6), len(i6))
        self.assertEqual(t6.XsdLiteral(t6), e6)
        t6 = xsd.base64Binary(e6)
        self.assertEqual(t6, i6)
        self.assertEqual(len(t6), len(i6))
        self.assertEqual(t6.XsdLiteral(t6), e6)

        i7 = "foobar"
        e7 = u"Zm9vYmFy"
        t7 = xsd.base64Binary(i7)
        self.assertEqual(t7, i7)
        self.assertEqual(len(t7), len(i7))
        self.assertEqual(t7.XsdLiteral(t7), e7)
        t7 = xsd.base64Binary(e7)
        self.assertEqual(t7, i7)
        self.assertEqual(len(t7), len(i7))
        self.assertEqual(t7.XsdLiteral(t7), e7)

if __name__ == '__main__':
    unittest.main()
