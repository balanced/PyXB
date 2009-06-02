import pyxb
import pyxb.binding.generate
import pyxb.utils.domutils

from xml.dom import Node

import os.path
schema_path = '%s/../schemas/xsi-type.xsd' % (os.path.dirname(__file__),)
code = pyxb.binding.generate.GeneratePython(schema_file=schema_path)

rv = compile(code, 'test', 'exec')
eval(rv)

from pyxb.exceptions_ import *

import unittest

class TestXSIType (unittest.TestCase):
    def testFailsNoType (self):
        xml = '<elt/>'
        doc = pyxb.utils.domutils.StringToDOM(xml)
        self.assertRaises(pyxb.AbstractInstantiationError, CreateFromDOM, doc.documentElement)

    def testDirect (self):
        xml = '<notAlt attrOne="low"><first>content</first></notAlt>'
        doc = pyxb.utils.domutils.StringToDOM(xml)
        instance = CreateFromDOM(doc.documentElement)
        self.assertEqual('content', instance.first().content())
        self.assertEqual('low', instance.attrOne())

    def testSubstitutions (self):
        xml = '<elt attrOne="low" xsi:type="alt1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><first>content</first></elt>'
        doc = pyxb.utils.domutils.StringToDOM(xml)
        instance = CreateFromDOM(doc.documentElement)
        self.assertEqual('content', instance.first().content())
        self.assertEqual('low', instance.attrOne())
        xml = '<elt attrTwo="hi" xsi:type="alt2" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><second/></elt>'
        doc = pyxb.utils.domutils.StringToDOM(xml)
        instance = CreateFromDOM(doc.documentElement)
        self.assertTrue(instance.second() is not None)
        self.assertEqual('hi', instance.attrTwo())

    def testMultilevel (self):
        xml = '<concreteBase><basement>dirt floor</basement></concreteBase>'
        doc = pyxb.utils.domutils.StringToDOM(xml)
        instance = CreateFromDOM(doc.documentElement)
        self.assertEqual('dirt floor', instance.basement().content())
        xml = '<oneFloor xsi:type="restaurant" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"><basement>concrete</basement><lobby>tiled</lobby><room>eats</room></oneFloor>'
        doc = pyxb.utils.domutils.StringToDOM(xml)
        instance = CreateFromDOM(doc.documentElement)
        self.assertEqual(concreteBase_.basement, instance.content().__class__.basement)
        self.assertEqual(oneFloor_.lobby, instance.content().__class__.lobby)
        self.assertEqual(restaurant.room, instance.content().__class__.room)
        self.assertEqual('tiled', instance.lobby().content())
        self.assertEqual('eats', instance.room().content())

if __name__ == '__main__':
    unittest.main()
    
        