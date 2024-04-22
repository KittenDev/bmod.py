import os
import sys

lib_pth = os.getcwd() + 'bmod/mesh'

if lib_pth not in sys.path:
    sys.path.append(lib_pth)
