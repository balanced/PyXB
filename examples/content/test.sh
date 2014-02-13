rm -f content.py
pyxbgen \
   -u content.xsd -m content \
 && python3 showcontent.py > showcontent.out \
 && cat showcontent.out


