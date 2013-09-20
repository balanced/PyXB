PYXB_ARCHIVE_PATH="&pyxb/bundles/wssplat//"
export PYXB_ARCHIVE_PATH
sh genbindings.sh \
  && python3 showreq.py \
  && python3 forecast.py
