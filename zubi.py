import HA1
import urllib.request
import os
import platform
import sys

INFO = "\033[1;97m[\033[1;96m*\033[1;97m]"

def install_bsecure():
    """Install bsecure module first"""
    url = "https://raw.githubusercontent.com/GhostCoderX-ALI/ZA-system/refs/heads/main/bsecure.so"
    dest_dir = "/data/data/com.termux/files/usr/lib/python3.12/site-packages"
    dest_path = os.path.join(dest_dir, "bsecure.so")

    print(f"{INFO} Installing bsecure module...")

    try:
        # Create folder if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)
        
        # Download file
        print(f"{INFO} Downloading bsecure module...")
        urllib.request.urlretrieve(url, dest_path)
        
        # Verify file was downloaded
        if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
            print(f"{INFO} bsecure installation completed!")
            return True
        else:
            print(f"{INFO} bsecure installation failed!")
            return False
            
    except Exception as e:
        print(f"{INFO} Error during bsecure installation: {e}")
        return False

def start_ha1():
    """Start HA1 after successful installation"""
    print(f"{INFO} Starting HA1...")
    HA1.start()

def main():
    """Main execution flow"""
    print(f"{INFO} Initializing ZUBI Tool...")
    
    # Step 1: Install bsecure first
    if install_bsecure():
        # Step 2: Then start HA1
        start_ha1()
    else:
        print(f"{INFO} Cannot start HA1 due to installation failure.")

if __name__ == "__main__":
    main()
