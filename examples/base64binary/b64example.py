"""Example usage of base64Binary.

A base64Binary XML schema field, when created from
python is assumed to be a binary string iff the
passed data type is 'str'.  If the passed data type
is unicode the value is assumed to be in lexical
representation (as found in the XML document) and
is treated as already being base64 encoded.

The base64binary type, when treated as a string,
yields the decoded binary data.

A non-obvious rule is the length constraint.
According to http://www.w3.org/TR/xmlschema-2/, 
section 4.3.1.3, the following holds true:
"if {primitive type definition} is hexBinary or
base64Binary, then the length of the value, as
measured in octets of the binary data, must be
equal to {value}". This is the reason that
the XsdValueLength class method returns the
length of the decoded binary data.
"""
import example
import base64

TEST_NAME = "test datum"
TEST_INDEX = 1
TEST_DECODED = "this is a test of encoded base64 data"
TEST_ENCODED = unicode(base64.b64encode(TEST_DECODED))

x = example.CreateFromDocument(file('example.xml').read())
assert x.name == TEST_NAME
assert x.index == 1
assert x.bytes == TEST_DECODED

y = example.Datum()
y.name = TEST_NAME
y.index = TEST_INDEX
y.bytes = TEST_DECODED

assert x.toxml() == y.toxml()

z = example.Datum()
z.name = TEST_NAME
z.index = TEST_INDEX
z.bytes = TEST_ENCODED

assert z.toxml() == x.toxml()
assert z.bytes == TEST_DECODED
assert z.bytes.XsdLiteral(z.bytes) == TEST_ENCODED
assert z.bytes.XsdValueLength(z.bytes) == len(TEST_DECODED)
