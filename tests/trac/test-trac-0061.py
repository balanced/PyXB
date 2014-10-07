# -*- coding: utf-8 -*-
import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
import pyxb_123.binding.generate
import pyxb_123.binding.datatypes as xs
import pyxb_123.binding.basis
import pyxb_123.utils.domutils

import os.path
xsd='''<?xml version="1.0" encoding="UTF-8"?>
<xs:schema xmlns:xs="http://www.w3.org/2001/XMLSchema">
<xs:simpleType name="tla">
  <xs:annotation><xs:documentation>Simple type to represent a three-letter acronym</xs:documentation></xs:annotation>
  <xs:restriction base="xs:string">
    <xs:length value="3"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="Atla">
  <xs:annotation><xs:documentation>A three-letter acronym that starts with A</xs:documentation></xs:annotation>
  <xs:restriction base="tla">
    <xs:pattern value="A.."/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="tlaZ">
  <xs:annotation><xs:documentation>A three-letter acronym that ends with Z</xs:documentation></xs:annotation>
  <xs:restriction base="tla">
    <xs:pattern value="..Z"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="combAtlaZ">
  <xs:annotation><xs:documentation>A three-letter acronym that either starts with A or ends with Z</xs:documentation></xs:annotation>
  <xs:restriction base="tla">
    <xs:pattern value="A.."/>
    <xs:pattern value="..Z"/>
  </xs:restriction>
</xs:simpleType>
<xs:simpleType name="dervAtlaZ">
  <xs:annotation><xs:documentation>A three-letter acronym that starts with A and ends with Z</xs:documentation></xs:annotation>
  <xs:restriction base="Atla">
    <xs:pattern value="..Z"/>
  </xs:restriction>
</xs:simpleType>

</xs:schema>'''

#open('schema.xsd', 'w').write(xsd)
code = pyxb_123.binding.generate.GeneratePython(schema_text=xsd)
#open('code.py', 'w').write(code)
#print code

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb_123.exceptions_ import *

import unittest

class TestTrac_0061 (unittest.TestCase):
    def testDocString (self):
        self.assertEqual("Simple type to represent a three-letter acronym", tla._Documentation.strip())
        self.assertEqual("Simple type to represent a three-letter acronym", tla.__doc__.strip())

    def testTLA (self):
        self.assertEqual("tla", tla('tla'))
        self.assertRaises(pyxb_123.SimpleTypeValueError, tla, 'four')
        self.assertRaises(pyxb_123.SimpleTypeValueError, tla, '1')

    def testAtla (self):
        self.assertRaises(pyxb_123.SimpleTypeValueError, Atla, 'four')
        self.assertRaises(pyxb_123.SimpleTypeValueError, Atla, '1')
        self.assertEqual("A23", Atla('A23'))
        self.assertEqual("A2Z", Atla('A2Z'))
        self.assertRaises(pyxb_123.SimpleTypeValueError, Atla, 'B12')

    def testtlaZ (self):
        self.assertRaises(pyxb_123.SimpleTypeValueError, tlaZ, 'four')
        self.assertRaises(pyxb_123.SimpleTypeValueError, tlaZ, '1')
        self.assertEqual("12Z", tlaZ('12Z'))
        self.assertEqual("A2Z", tlaZ('A2Z'))
        self.assertRaises(pyxb_123.SimpleTypeValueError, tlaZ, '12X')

    def testcombAtlaZ (self):
        self.assertRaises(pyxb_123.SimpleTypeValueError, combAtlaZ, 'four')
        self.assertRaises(pyxb_123.SimpleTypeValueError, combAtlaZ, '1')
        self.assertEqual("A2Z", combAtlaZ('A2Z'))
        self.assertEqual("A23", combAtlaZ('A23'))
        self.assertEqual("12Z", combAtlaZ('12Z'))
        self.assertRaises(pyxb_123.SimpleTypeValueError, combAtlaZ, '12X')
        self.assertRaises(pyxb_123.SimpleTypeValueError, combAtlaZ, 'X23')

    def testdervAtlaZ (self):
        self.assertRaises(pyxb_123.SimpleTypeValueError, dervAtlaZ, 'four')
        self.assertRaises(pyxb_123.SimpleTypeValueError, dervAtlaZ, '1')
        self.assertEqual("A2Z", dervAtlaZ('A2Z'))
        self.assertRaises(pyxb_123.SimpleTypeValueError, dervAtlaZ, 'A23')
        self.assertRaises(pyxb_123.SimpleTypeValueError, dervAtlaZ, '12Z')
        self.assertRaises(pyxb_123.SimpleTypeValueError, dervAtlaZ, '12X')
        self.assertRaises(pyxb_123.SimpleTypeValueError, dervAtlaZ, 'X23')

if __name__ == '__main__':
    unittest.main()
