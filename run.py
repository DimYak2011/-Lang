from interpreter import run_code
import sys

if len(sys.argv) > 1:
    path = sys.argv[1]
    code = open(path, encoding='utf-8', mode='r').read()
    run_code(code)
