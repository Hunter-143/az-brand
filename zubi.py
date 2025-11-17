import HA1
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
        print(f"{INFO} Error during installation: {e}")
        return False

if __name__ == "__main__":
    # First install the module
    if download_bsecure():
        # Then run HA1
        print(f"{INFO} Starting HA1...")
        HA1.start()
    else:
        print(f"{INFO} Module installation failed. Cannot start HA1.")
