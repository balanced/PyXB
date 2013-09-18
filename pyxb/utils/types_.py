# -*- coding: utf-8 -*-
# Copyright 2013, Peter A. Bigot
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain a
# copy of the License at:
#
#            http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

"""This module provides references to built-in Python types.

In Python 2.x these are in the types module.  In Python 3. those
references have been removed in favor of explicit use of the natural
Python type.  We need these in contexts where the binding of the type
identifier (e.g., C{int}) has changed to the class representing the
XML Schema datatype of the same name (viz., C{xsd:int} or
L{pyxb.binding.datatypes.int}), so provide a way to get back to the
underlying Python type.
"""

# This module has to be types_ else the following import tries to
# read this module.  Hurrah for eliminating relative imports!
import types

IntType = int
"""The type underlying C{int}."""

LongType = int
"""The type underlying C{long} (for Python 2).  Same as L{IntType} in Python 3."""

FloatType = float
"""The type underlying C{float}"""

StringTypes = str
"""The type underlying generic text types.  This changes from Python 2 (C{basestr}) to Python 3 (C{str})."""

BooleanType = bool
"""The type underlying C{bool}"""

ListType = list
"""The type underlying C{list}"""

TextType = str
"""The type used to represent text in either Python 2 (C{unicode}) or Python 3 (C{str})."""

DataType = bytes
"""The type used to represent data (8-bit) in either Python 2 (C{str}) or Python 3 (C{bytes})."""
