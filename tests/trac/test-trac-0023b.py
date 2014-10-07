# -*- coding: utf-8 -*-
import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
# Declare xml namespace
import pyxb_123.binding.generate
import pyxb_123.utils.domutils
from xml.dom import Node

import os.path

xsd='''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns:xml="http://www.w3.org/XML/1998/namespace">
  <xs:complexType name="structure">
    <xs:attributeGroup ref="xml:specialAttrs"/>
  </xs:complexType>
  <xs:element name="instance" type="structure"/>
</xs:schema>'''

code = pyxb_123.binding.generate.GeneratePython(schema_text=xsd)
#open('code.py', 'w').write(code)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_123.exceptions_ import *

import unittest

class TestTrac0023 (unittest.TestCase):
    def testBasic (self):
        self.assertEqual(4, len(structure._AttributeMap))
        self.assertEqual(pyxb_123.binding.xml_.STD_ANON_lang, structure._AttributeMap[pyxb_123.namespace.XML.createExpandedName('lang')].dataType())
        self.assertEqual(pyxb_123.binding.xml_.STD_ANON_space, structure._AttributeMap[pyxb_123.namespace.XML.createExpandedName('space')].dataType())
        self.assertEqual(pyxb_123.binding.datatypes.anyURI, structure._AttributeMap[pyxb_123.namespace.XML.createExpandedName('base')].dataType())
        self.assertEqual(pyxb_123.binding.datatypes.ID, structure._AttributeMap[pyxb_123.namespace.XML.createExpandedName('id')].dataType())

if __name__ == '__main__':
    unittest.main()

