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
  <xs:redefine/>
</xs:schema>'''

from pyxb_123.exceptions_ import *

import unittest

class TestTrac_0093 (unittest.TestCase):
    def testRedefine (self):
        self.assertRaises(pyxb.IncompleteImplementationError, pyxb.binding.generate.GeneratePython, schema_text=xsd)

if __name__ == '__main__':
    unittest.main()
