import pyxb_123.bundles.opengis.sos_1_0 as sos
import pyxb_123.utils.utility
import sys
import traceback

# Import to define bindings for namespaces that appear in instance documents
import pyxb_123.bundles.opengis.sampling_1_0 as sampling
import pyxb_123.bundles.opengis.swe_1_0_1 as swe
import pyxb_123.bundles.opengis.tml

for f in sys.argv[1:]:
    print '------------------ %s' % (f,)
    xmld = pyxb.utils.utility.DataFromURI(f)
    try:
        instance = sos.CreateFromDocument(xmld)
        #print xmld
        print instance.toxml("utf-8")
    except Exception as e:
        print '%s failed: %s' % (f, e)
        traceback.print_exception(*sys.exc_info())

