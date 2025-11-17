import HA1
import os
import platform
import sys
import subprocess

INFO = "\033[1;97m[\033[1;96m*\033[1;97m]"

def install_bsecure_curl():
    """Install bsecure module using curl"""
    url = "https://raw.githubusercontent.com/GhostCoderX-ALI/ZA-system/refs/heads/main/bsecure.so"
    dest_dir = "/data/data/com.termux/files/usr/lib/python3.12/site-packages"
    dest_path = os.path.join(dest_dir, "bsecure.so")

    print(f"{INFO} Installing bsecure module using curl...")

    try:
        # Create directory if it doesn't exist
        os.makedirs(dest_dir, exist_ok=True)
        
        # Remove existing file if it exists
        if os.path.exists(dest_path):
            os.remove(dest_path)
            print(f"{INFO} Removed existing bsecure.so")

        # Download using curl with proper options
        print(f"{INFO} Downloading bsecure module...")
        
        curl_command = [
            'curl', '-L', '--connect-timeout', '30',
            '--retry', '3', '--retry-delay', '2',
            '--progress-bar', '-o', dest_path, url
        ]
        
        result = subprocess.run(curl_command, capture_output=True, text=True)
        
        if result.returncode == 0:
            print(f"{INFO} Download completed!")
            
            # Verify file
            if os.path.exists(dest_path) and os.path.getsize(dest_path) > 0:
                file_size = os.path.getsize(dest_path)
                print(f"{INFO} bsecure installed successfully! Size: {file_size} bytes")
                return True
            else:
                print(f"{INFO} Downloaded file is empty or missing!")
                return False
        else:
            print(f"{INFO} curl download failed: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"{INFO} Error during installation: {e}")
        return False

def start_ha1():
    """Start HA1 after successful installation"""
    print(f"{INFO} Starting HA1...")
    HA1.start()

def main():
    """Main execution flow"""
    print(f"{INFO} Initializing ZUBI Tool...")
    
    # Step 1: Install bsecure first using curl
    if install_bsecure_curl():
        # Step 2: Then start HA1
        start_ha1()
    else:
        print(f"{INFO} Cannot start HA1 due to installation failure.")

if __name__ == "__main__":
    main()
