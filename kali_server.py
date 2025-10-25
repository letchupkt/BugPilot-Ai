#!/usr/bin/env python3
"""
Kali Security Server - Protected Version
Copyright (c) 2025 LAKSHMIKANTHAN K (letchupkt)

"""

import base64, zlib, sys

# Protected application data
_protected_data = [
    "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",
]

def _load_protected():
    """Load and execute protected code"""
    try:
        data = "".join(_protected_data)
        decoded = base64.b64decode(data.encode('ascii'))
        decompressed = zlib.decompress(decoded)
        code = decompressed.decode('utf-8')
        exec(code, globals())
    except Exception as e:
        print("ERROR: Protected code verification failed!")
        print("This software may have been tampered with.")
        sys.exit(1)

# Execute protected application
if __name__ == "__main__":
    _load_protected()
