# -*- coding: utf-8 -*-
import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
import pyxb_123
import pyxb_123.xmlschema.structures
import pyxb_123.utils.domutils

from pyxb_123.exceptions_ import *

import unittest

def CreateDocumentationNode (content):
    xmls = '<xs:annotation xmlns:xs="%s"><xs:documentation>%s</xs:documentation></xs:annotation>' % (pyxb_123.namespace.XMLSchema.uri(), content)
    dom = pyxb_123.utils.domutils.StringToDOM(xmls)
    node = dom.documentElement
    nsc = pyxb_123.namespace.resolution.NamespaceContext.GetNodeContext(node)
    if nsc.targetNamespace() is None:
        nsc.finalizeTargetNamespace()
    return pyxb_123.xmlschema.structures.Annotation.CreateFromDOM(node)


class TestTrac_0045 (unittest.TestCase):
    def testSimple (self):
        self.assertEqual('hi there!', CreateDocumentationNode("hi there!").asDocString())
        self.assertEqual(' "hi there!" ', CreateDocumentationNode('"hi there!"').asDocString())
        self.assertEqual("''' docstring! '''", CreateDocumentationNode('""" docstring! """').asDocString())
        self.assertEqual("inner ''' docstring!", CreateDocumentationNode('inner """ docstring!').asDocString())

if __name__ == '__main__':
    unittest.main()
