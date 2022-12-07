#!/usr/bin/python3

import atheris

with atheris.instrument_imports():
    from base58 import b58decode, b58encode
    import sys

def Fuzz(data):
    encoded = b58encode(data)
    decoded = b58decode(encoded)
    if decoded != data: 
        sys.exit(0)

if __name__ == '__main__':
    atheris.instrument_all()
    atheris.Setup(sys.argv, Fuzz)
    atheris.Fuzz()
