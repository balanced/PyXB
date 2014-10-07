# -*- coding: utf-8 -*-
import pyxb_123.bundles.common.xhtml1 as xhtml
import pyxb_123.utils.domutils
import xml.dom.minidom
from xml.dom import Node

pyxb.utils.domutils.BindingDOMSupport.SetDefaultNamespace(xhtml.Namespace)

ind = open('in.xhtml', 'rb').read()
i1 = xhtml.CreateFromDocument(ind)
xmld = i1.toDOM().toxml('utf-8')
open('out.xhtml', 'wb').write(xmld)
