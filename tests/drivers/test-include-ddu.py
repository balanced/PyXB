# -*- coding: utf-8 -*-
import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
import pyxb_123.binding.generate
import pyxb_123.utils.domutils

import os.path
schema_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schemas/test-include-ddu.xsd'))
code = pyxb_123.binding.generate.GeneratePython(schema_location=schema_path)
#open('code.py', 'w').write(code)
rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_123.exceptions_ import *

import unittest

class TestIncludeDD (unittest.TestCase):
    def setUp (self):
        self.__basis_log = logging.getLogger('pyxb_123.binding.basis')
        self.__basis_loglevel = self.__basis_log.level

    def tearDown (self):
        self.__basis_log.level = self.__basis_loglevel

    def testDefault (self):
        xmls = '<entry xmlns="%s"><from>one</from><to>single</to></entry>' % (Namespace.uri(),)
        # Default namespace applies to from which should be in no namespace
        self.__basis_log.setLevel(logging.ERROR)
        self.assertRaises(pyxb_123.UnrecognizedContentError, CreateFromDocument, xmls.encode('utf-8'))

    def testExplicit (self):
        xmls = '<ns:entry xmlns:ns="%s"><from>one</from><ns:to>single</ns:to></ns:entry>' % (Namespace.uri(),)
        instance = CreateFromDocument(xmls.encode('utf-8'))
        self.assertEqual(english.one, instance.from_)

if __name__ == '__main__':
    unittest.main()

