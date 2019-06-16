import os
import sys

try:
    if os.stat('690.jpg').st_size < 10000:
        raise MemoryError("Image is oversized")
    else:
        print("Everything is fine")
except Exception as e:
    sys.stderr.write(str(e))