#!/usr/bin/env python3
import sys
import subprocess
import os
import platform

def print_header(text):
    print("\n" + "="*50)
    print(text)
    print("="*50 + "\n")

def check_python_version():
    print("[1/5] Checking Python version...")
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print(f"❌ Python {version.major}.{version.minor} detected")
        print("   Python 3.8 or higher is required")
        return False
    print(f"✓ Python {version.major}.{version.minor}.{version.micro} detected")
    return True

def check_pip():
    print("\n[2/5] Checking pip installation...")
    try:
        result = subprocess.run([sys.executable, "-m", "pip", "--version"], 
                              capture_output=True, text=True, check=True)
        print("✓ pip is installed")
        print(f"  {result.stdout.strip()}")
        return True
    except subprocess.CalledProcessError:
        print("❌ pip is not installed")
        return False

def install_requirements():
    print("\n[3/5] Installing required packages...")
    print("This may take a few minutes...\n")
    
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "--upgrade", "pip"],
                      check=True)
        print("✓ pip upgraded")
        
        if not os.path.exists("requirements.txt"):
            print("❌ requirements.txt not found!")
            return False
            
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                      check=True)
        print("\n✓ All packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"\n❌ Error installing packages: {e}")
        print("   Please check your internet connection")
        return False

def check_chrome():
    print("\n[4/5] Checking Google Chrome installation...")
    
    chrome_paths = []
    if platform.system() == "Windows":
        chrome_paths = [
            r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
        ]
    elif platform.system() == "Darwin":
        chrome_paths = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        ]
    else:
        chrome_paths = [
            "/usr/bin/google-chrome",
            "/usr/bin/chromium",
            "/usr/bin/chromium-browser"
        ]
    
    for path in chrome_paths:
        if os.path.exists(path):
            print(f"✓ Chrome found at: {path}")
            return True
    
    print("⚠️  Google Chrome not found")
    print("   Please install Chrome from: https://www.google.com/chrome/")
    print("   The script will still work if Chrome is installed elsewhere")
    return True

def verify_installation():
    print("\n[5/5] Verifying installation...")
    try:
        import selenium
        from selenium import webdriver
        from webdriver_manager.chrome import ChromeDriverManager
        
        print(f"✓ selenium {selenium.__version__} installed")
        print("✓ webdriver-manager installed")
        print("✓ All dependencies verified")
        return True
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False

def main():
    print_header("Eitaa Automation - Automatic Setup")
    print("This script will install all required dependencies")
    
    success = True
    
    if not check_python_version():
        success = False
    
    if success and not check_pip():
        success = False
    
    if success and not install_requirements():
        success = False
    
    if success:
        check_chrome()
    
    if success and not verify_installation():
        success = False
    
    print_header("Setup Complete!" if success else "Setup Failed!")
    
    if success:
        print("✅ All dependencies installed successfully!\n")
        print("To run the automation script:")
        print("  python eitaa_automation.py")
        print("\nWith custom phone number:")
        print("  python eitaa_automation.py 9101234567")
        print()
    else:
        print("❌ Setup encountered errors")
        print("Please fix the issues above and run setup again")
        print()
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nSetup cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Unexpected error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
