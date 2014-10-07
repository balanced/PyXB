from __future__ import print_function
xml_file = 'ipo.xml'

import pyxb_123.binding.saxer
import ipo

def ShowOrder (order):
    print('%s is sending %s %d thing(s):' % (order.billTo().name(), order.shipTo().name(), len(order.items().item())))
    for item in order.items().item():
        print('  Quantity %d of %s at $%s' % (item.quantity(), item.productName(), item.USPrice()))

if False:
    import pyxb_123.utils.domutils
    xmld = pyxb_123.utils.domutils.StringToDOM(open(xml_file).read())
    dom_value = ipo.CreateFromDOM(xmld.documentElement)
    ShowOrder(dom_value)

saxer = pyxb_123.binding.saxer.make_parser()
handler = saxer.getContentHandler()
saxer.parse(open(xml_file))
ShowOrder(handler.rootObject())
