# -*- coding: utf-8 -*-
import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
import pyxb_123.binding.generate
import pyxb_123.utils.domutils

import os.path
schema_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schemas/test-include-ddq.xsd'))
code = pyxb_123.binding.generate.GeneratePython(schema_location=schema_path)
#open('code.py', 'w').write(code)
rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_123.exceptions_ import *

import unittest

class TestIncludeDD (unittest.TestCase):
    def testDefault (self):
        xmls = '<entry xmlns="%s"><from>one</from><to>single</to></entry>' % (Namespace.uri(),)
        instance = CreateFromDocument(xmls.encode('utf-8'))
        self.assertEqual(english.one, instance.from_)

    def testExplicit (self):
        xmls = '<ns:entry xmlns:ns="%s"><ns:from>one</ns:from><ns:to>single</ns:to></ns:entry>' % (Namespace.uri(),)
        instance = CreateFromDocument(xmls.encode('utf-8'))
        self.assertEqual(english.one, instance.from_)

if __name__ == '__main__':
    unittest.main()

