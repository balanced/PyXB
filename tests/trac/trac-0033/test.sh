fail () {
  echo 1>&2 "${test_name} FAILED: ${@}"
  exit 1
}

python3 tread.py || fail trac33
echo 'trac33 passed'
