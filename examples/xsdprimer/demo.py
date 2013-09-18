
import pyxb
import ipo
import xml.dom.minidom
import time
import io

xmld = open('ipo.xml', 'rb').read()

order = ipo.CreateFromDOM(xml.dom.minidom.parse(io.BytesIO(xmld)).documentElement)

print('%s is sending %s %d thing(s):' % (order.billTo().name(), order.shipTo().name(), len(list(order.items()).item())))
for item in list(order.items()).item():
    print('  Quantity %d of%s at $%s' % (item.quantity(), item.productName(), item.USPrice()))

# Give Mary more
try:
    item.setQuantity(100)
except pyxb.SimpleTypeValueError as e:
    print('Too many: %s' % (e,))
    item.setQuantity(10)
print('Increased quantity to %d' % (item.quantity(),))
