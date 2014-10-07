# -*- coding: utf-8 -*-
import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
import xml.dom.minidom
import pyxb_123.utils.domutils

import unittest

class TestTrac0156a (unittest.TestCase):
    def testLocateUnique (self):
        dom = xml.dom.minidom.parseString(u'<xs:simpleType xmlns:xs="http://www.w3.org/2001/XMLSchema"><xs:list>x</xs:list></xs:simpleType>')
        x = pyxb_123.utils.domutils.LocateUniqueChild (dom.firstChild, 'list')
        dom = xml.dom.minidom.parseString(u'<xs:simpleType xmlns:xs="http://www.w3.org/2001/XMLSchema"><xs:list>x</xs:list><xs:list>x</xs:list></xs:simpleType>')
        self.assertRaises(pyxb_123.SchemaValidationError, pyxb_123.utils.domutils.LocateUniqueChild, dom.firstChild, 'list')
        dom = xml.dom.minidom.parseString(u'<xs:simpleType xmlns:xs="http://www.w3.org/2001/XMLSchema"><xs:lit>x</xs:lit></xs:simpleType>')
        self.assertRaises(pyxb_123.SchemaValidationError, pyxb_123.utils.domutils.LocateUniqueChild, dom.firstChild, 'list', absent_ok=False)

if __name__ == '__main__':
    unittest.main()

