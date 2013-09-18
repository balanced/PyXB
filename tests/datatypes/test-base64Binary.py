# -*- coding: utf-8 -*-
import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
import unittest
import binascii
import pyxb
import pyxb.binding.datatypes as xsd

class Test_base64Binary (unittest.TestCase):
    RFC4648_S9 = ( ('14fb9c03d97e', 'FPucA9l+'),
                   ('14fb9c03d9', 'FPucA9k='),
                   ('14fb9c03', 'FPucAw==') )
    RFC4648_S10 = ( ('', ''),
                    ('f', 'Zg=='),
                    ('fo', 'Zm8='),
                    ('foo', 'Zm9v'),
                    ('foob', 'Zm9vYg=='),
                    ('fooba', 'Zm9vYmE='),
                    ('foobar', 'Zm9vYmFy') )
    def testVectors (self):
        """RFC4648 section 10."""
        for (plaintext, ciphertext) in self.RFC4648_S10:
            plaintexd = plaintext.encode('utf-8')
            ciphertexd = ciphertext.encode('utf-8')
            self.assertEqual(xsd.base64Binary(plaintexd).xsdLiteral(), ciphertext)
            self.assertEqual(xsd.base64Binary(ciphertext, _from_xml=True), plaintexd)
        for (hextext, ciphertext) in self.RFC4648_S9:
            hextexd = hextext.encode('utf-8')
            plaintexd = binascii.unhexlify(hextexd)
            self.assertEqual(xsd.base64Binary(plaintexd).xsdLiteral(), ciphertext)
            self.assertEqual(xsd.base64Binary(ciphertext, _from_xml=True), plaintexd)

    def testInvalid (self):
        self.assertRaises(pyxb.SimpleTypeValueError, xsd.base64Binary, 'Z', _from_xml=True)
        self.assertRaises(pyxb.SimpleTypeValueError, xsd.base64Binary, 'Zg', _from_xml=True)
        self.assertRaises(pyxb.SimpleTypeValueError, xsd.base64Binary, 'Zg=', _from_xml=True)
        self.assertEqual('f'.encode('utf-8'), xsd.base64Binary('Zg==', _from_xml=True))
        self.assertRaises(pyxb.SimpleTypeValueError, xsd.base64Binary, 'ZZZ=', _from_xml=True)
        self.assertRaises(pyxb.SimpleTypeValueError, xsd.base64Binary, 'ZZ==', _from_xml=True)
        self.assertRaises(pyxb.SimpleTypeValueError, xsd.base64Binary, 'ZE==', _from_xml=True)

if __name__ == '__main__':
    unittest.main()
