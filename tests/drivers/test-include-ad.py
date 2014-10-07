# -*- coding: utf-8 -*-
import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
import pyxb_123.binding.generate
import pyxb_123.utils.domutils

import os.path

from pyxb_123.exceptions_ import *

import unittest

class TestIncludeDD (unittest.TestCase):
    def testDefault (self):
        schema_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../schemas/test-include-ad.xsd'))
        self.assertRaises(pyxb_123.SchemaValidationError, pyxb_123.binding.generate.GeneratePython, schema_location=schema_path)

if __name__ == '__main__':
    unittest.main()

