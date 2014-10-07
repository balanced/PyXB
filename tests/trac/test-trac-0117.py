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
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
  <xs:simpleType name="tABCD">
    <xs:restriction base="xs:normalizedString">
      <xs:enumeration value="A"/>
      <xs:enumeration value="B"/>
      <xs:enumeration value="C"/>
      <xs:enumeration value="D"/>
    </xs:restriction>
  </xs:simpleType>
  <xs:element name="Element">
   <xs:complexType name="tElement">
     <xs:attribute name="attr" type="tABCD"/>
     <xs:attribute name="Required" type="xs:string" use="required"/>
   </xs:complexType>
  </xs:element>
</xs:schema>'''

code = pyxb_123.binding.generate.GeneratePython(schema_text=xsd)
#open('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_123.exceptions_ import *

import unittest

class TestTrac0117 (unittest.TestCase):
    def tearDown (self):
        pyxb_123.RequireValidWhenGenerating(True)
        pyxb_123.RequireValidWhenParsing(True)

    def testRequired (self):
        xmls = '<Element/>'
        pyxb_123.RequireValidWhenParsing(True)
        self.assertRaises(MissingAttributeError, CreateFromDocument, xmls)
        pyxb_123.RequireValidWhenParsing(False)
        self.assertFalse(pyxb_123._ParsingRequiresValid)
        instance = CreateFromDocument(xmls)
        self.assertEqual(None, instance.attr)

    def testEnumeration (self):
        pyxb_123.RequireValidWhenParsing(True)
        xmls = '<Element Required="true" attr="Q"/>'
        self.assertRaises(pyxb_123.SimpleTypeValueError, CreateFromDocument, xmls)
        pyxb_123.RequireValidWhenParsing(False)
        instance = CreateFromDocument(xmls)
        self.assertEqual('Q', instance.attr)

    def testGood (self):
        pyxb_123.RequireValidWhenParsing(True)
        xmls = '<Element Required="true" attr="D"/>'
        instance = CreateFromDocument(xmls)
        self.assertEqual('D', instance.attr)
        self.assertTrue(instance.Required)

if __name__ == '__main__':
    unittest.main()

