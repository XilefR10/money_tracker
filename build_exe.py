#!/usr/bin/env python
"""
Build script to create a standalone Money Tracker executable.
Run this script to generate main.exe in the dist/ folder.
"""

import subprocess
import sys
import os

def main():
    print("=" * 60)
    print("Money Tracker - Building Standalone Executable")
    print("=" * 60)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("\n[*] PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    print("\n[*] Building executable...")
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--name=MoneyTracker",
        "main.py"
    ]
    
    result = subprocess.run(cmd, cwd=os.path.dirname(os.path.abspath(__file__)))
    
    if result.returncode == 0:
        print("\n" + "=" * 60)
        print("[✓] Build successful!")
        print("=" * 60)
        print("\nYour executable is ready:")
        exe_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "dist", "MoneyTracker.exe")
        print(f"  Location: {exe_path}")
        print(f"\nYou can now:")
        print(f"  - Run it directly by double-clicking MoneyTracker.exe")
        print(f"  - Move it to any folder on your PC")
        print(f"  - Create a shortcut on your desktop")
        print(f"\nNote: Keep data.json in the same folder as the .exe to save entries.")
    else:
        print("\n[✗] Build failed. Check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
