import os, platform, time, pycurl
os.system('clear')
print('checking updates')
os.system('git pull')
print('first allow permations (y)')
os.system('termux-setup-storage')
try:
    import requests
except:
    os.system('pip install requests')
try:
    import pycurl
except:
    os.system('pip install pycurl')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support This Tool")
    from FKING import menu___
    menu___()
