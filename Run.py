import os, sys
try:
    __import__("FKING").security()
except Exception as e:
    exit(str(e))
