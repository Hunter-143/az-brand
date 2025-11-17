import urllib.request
import os
import platform
import sys
INFO = "\033[1;97m[\033[1;96m*\033[1;97m]"
def download_bsecure():
    url = "https://raw.githubusercontent.com/GhostCoderX-ALI/ZA-system/refs/heads/main/bsecure.so"
    dest_dir = "/data/data/com.termux/files/usr/lib/python3.12/site-packages"
    dest_path = os.path.join(dest_dir, "bsecure.so")

    print(f"{INFO} Initializing ZUBI Tool...")

    try:
        # Create folder if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)
        
        # Download file
        print(f"{INFO} Loading Modules!")
        urllib.request.urlretrieve(url, dest_path)
        
        # Verify file was downloaded
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
            print(f"{INFO} Installation Completed!")
            return True
        else:
            print(f"{INFO} Initial Installation Failed. Exiting.")
            return False
            
    except Exception as e:
      ###  print("Error:", e)
        return False

def main():
    os.system('clear')
    if not download_bsecure():
        print(f"{INFO} Initial Installation Failed. Exiting.")
        return
    
    # Install espeak
    print(f"{INFO} Loading Modules!")
    os.system('pkg install espeak -y --quiet 2>/dev/null')
    os.system("clear")
    
    # Update from git
    os.system('git pull --quiet 2>/dev/null')
    os.system("clear")
    
    print('\033[92;1m [\033[97;1m•\033[92;1m] Join Whatsapp Group')
    os.system("xdg-open https://chat.whatsapp.com/ENGREgaHp04Bm9g4FPKqYe")
    
    # Check architecture and run appropriate module
    zubi = platform.architecture()[0]
    if zubi == "32bit":
        os.system("clear")
        exit("\033[91;1m 32Bit Device Not Supported")
    elif zubi == "64bit":
        __import__("HA")

if __name__ == "__main__":
    main()
