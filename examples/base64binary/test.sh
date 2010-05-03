rm -f example.py
pyxbgen \
   -u example.xsd -m example \
 && python b64example.py
