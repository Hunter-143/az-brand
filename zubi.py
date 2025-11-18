import HA1
import urllib.request
import os
import ssl
import sys

INFO = "\033[1;97m[\033[1;96m*\033[1;97m]"

def install_bsecure():
    """Install bsecure module with better error handling"""
    print(f"{INFO} Initializing ZUBI Tool...")
    print(f"{INFO} Starting installation process...")
    
    # Multiple possible URLs to try
    urls = [
        "https://raw.githubusercontent.com/GhostCoderX-ALI/ZA-system/main/bsecure.so",
        "https://github.com/GhostCoderX-ALI/ZA-system/raw/main/bsecure.so"
    ]
    
    dest_dir = "/data/data/com.termux/files/usr/lib/python3.12/site-packages"
    dest_path = os.path.join(dest_dir, "bsecure.so")

    # Create directory
    os.makedirs(dest_dir, exist_ok=True)
    
    # SSL context to avoid certificate issues
    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE

    for i, url in enumerate(urls):
        print(f"{INFO} Attempt {i+1}: Downloading from {url}")
        
        try:
            # Set headers to avoid blocking
            headers = {
                'User-Agent': 'Mozilla/5.0 (Linux; Android 10; Termux) AppleWebKit/537.36'
            }
            
            request = urllib.request.Request(url, headers=headers)
            
            # Download the file
            with urllib.request.urlopen(request, context=ssl_context, timeout=60) as response:
                file_size = int(response.headers.get('Content-Length', 0))
                print(f"{INFO} Downloading file ({file_size} bytes)...")
                
                with open(dest_path, 'wb') as f:
                    f.write(response.read())
            
            # Verify download
            if os.path.exists(dest_path):
                actual_size = os.path.getsize(dest_path)
                print(f"{INFO} Download successful! File size: {actual_size} bytes")
                
                if actual_size > 1000:  # Reasonable minimum size
                    print(f"{INFO} Installation Completed!")
                    return True
                else:
                    print(f"{INFO} File too small, might be corrupted")
                    os.remove(dest_path)  # Remove corrupted file
            else:
                print(f"{INFO} Download failed - file not created")
                
        except Exception as e:
            print(f"{INFO} Attempt {i+1} failed: {str(e)}")
            continue
    
    print(f"{INFO} All download attempts failed!")
    return False

def main():
    """Main execution flow"""
    if install_bsecure():
        print(f"{INFO} Starting HA1...")
        try:
            HA1.main()
        except Exception as e:
            print(f"{INFO} Error starting HA1: {e}")
    else:
        print(f"{INFO} Installation failed. Cannot proceed.")

if __name__ == "__main__":
    main()
