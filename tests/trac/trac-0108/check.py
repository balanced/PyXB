#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging
if __name__ == '__main__':
    logging.basicConfig()
_log = logging.getLogger(__name__)
import TestPatternRestriction as t

xml="\U00010314"
p = t.test(xml)
print(p.toxml("utf-8"))
