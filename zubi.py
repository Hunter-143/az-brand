import os,platform
os.system('pkg install espeak -y --quiet 2>/dev/null')
os.system("clear")
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[92;1m [\033[97;1m•\033[92;1m] Join Whatsapp Group')
os.system("xdg-open https://chat.whatsapp.com/ENGREgaHp04Bm9g4FPKqYe")
zubi=platform.architecture()[0]
if zubi=="32bit":
    os.system("clear");exit("\033[91;1m 32Bit Device Not Supported")
    __import__("HA1")
elif zubi=="64bit":
    __import__("HA1")
