rm -f cablelabs.wxs
sh genbindings.sh \
  && python3 demo.py
