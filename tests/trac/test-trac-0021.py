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
  <xs:element name="elt" type="xs:string"/>
  <xs:complexType name="empty"/>
  <xs:complexType name="simple">
    <xs:simpleContent>
      <xs:extension base="xs:string"/>
    </xs:simpleContent>
  </xs:complexType>
  <xs:complexType name="complex">
    <xs:sequence>
      <xs:element ref="elt"/>
    </xs:sequence>
  </xs:complexType>
</xs:schema>'''

code = pyxb_123.binding.generate.GeneratePython(schema_text=xsd)
#print code

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_123.exceptions_ import *

import unittest

class TestTrac0021 (unittest.TestCase):
    """Presence of a wildcard in a sequence model group causes other
    elements in that group to not be generated."""
    def testEmpty (self):
        instance = empty()
        self.assertRaises(pyxb_123.NotSimpleContentError, instance.value)
        self.assertRaises(pyxb_123.NotComplexContentError, instance.orderedContent)

    def testSimple (self):
        instance = simple("hi")
        self.assertEqual("hi", instance.value())
        self.assertRaises(pyxb_123.NotComplexContentError, instance.orderedContent)

    def testComplex (self):
        instance = complex("hi")
        self.assertRaises(pyxb_123.NotSimpleContentError, instance.value)
        elt = instance.orderedContent()[0]
        self.assertTrue(isinstance(elt.value, basestring))
        self.assertEqual("hi", elt.value)


if __name__ == '__main__':
    unittest.main()

