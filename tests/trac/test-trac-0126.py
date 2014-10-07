# -*- coding: utf-8 -*-
import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
import pyxb_123.binding.generate
import pyxb_123.utils.domutils
from xml.dom import Node

import os.path
xsd='''<?xml version="1.0" encoding="UTF-8"?>
<schema xmlns="http://www.w3.org/2001/XMLSchema">
  <element name="Element">
   <complexType name="tElement">
     <attribute name="Required" type="string" use="required"/>
     <attribute name="Optional" type="string" use="optional"/>
   </complexType>
  </element>
</schema>'''

code = pyxb_123.binding.generate.GeneratePython(schema_text=xsd)
#open('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_123.exceptions_ import *

import unittest

class TestTrac0126 (unittest.TestCase):
    def tearDown (self):
        pyxb_123.RequireValidWhenGenerating(True)
        pyxb_123.RequireValidWhenParsing(True)

    def testBasic (self):
        instance = Element()
        self.assertEqual(None, instance.Required)
        self.assertEqual(None, instance.Optional)

        pyxb_123.RequireValidWhenGenerating(False)
        xmlt = u'<Element/>'
        xmld = xmlt.encode('utf-8')
        self.assertEqual(instance.toDOM().documentElement.toxml("utf-8"), xmld)
        pyxb_123.RequireValidWhenGenerating(True)
        self.assertRaises(pyxb_123.MissingAttributeError, instance.toDOM)
        instance.Required = 'value'
        xmlt = u'<Element Required="value"/>'
        xmld = xmlt.encode('utf-8')
        self.assertEqual(instance.toDOM().documentElement.toxml("utf-8"), xmld)


if __name__ == '__main__':
    unittest.main()

