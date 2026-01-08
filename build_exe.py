#!/usr/bin/env python
"""
Build script to create a standalone Money Tracker executable.
Run this script to generate MoneyTracker.exe in the dist/ folder.

Features:
- Cleans old build files before building
- Creates a standalone .exe file
- All dependencies are bundled into the executable
"""

import subprocess
import sys
import os
import shutil

def cleanup_old_builds(base_dir):
    """Remove old build artifacts."""
    print("\n[*] Cleaning old build files...")
    
    # Remove old dist folder contents
    dist_dir = os.path.join(base_dir, "dist")
    build_dir = os.path.join(base_dir, "build")
    
    for directory in [dist_dir, build_dir]:
        if os.path.exists(directory):
            try:
                shutil.rmtree(directory)
                print(f"    ✓ Removed {directory}")
            except Exception as e:
                print(f"    ⚠ Could not remove {directory}: {e}")
    
    # Remove spec file
    spec_file = os.path.join(base_dir, "MoneyTracker.spec")
    if os.path.exists(spec_file):
        try:
            os.remove(spec_file)
            print(f"    ✓ Removed {spec_file}")
        except Exception as e:
            print(f"    ⚠ Could not remove {spec_file}: {e}")

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    print("=" * 60)
    print("💰 Money Tracker - Building Standalone Executable")
    print("=" * 60)
    
    # Check if PyInstaller is installed
    try:
        import PyInstaller
    except ImportError:
        print("\n[*] PyInstaller not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
    
    # Clean old builds
    cleanup_old_builds(base_dir)
    
    print("\n[*] Building executable...")
    print("    This may take a few minutes...")
    
    cmd = [
        sys.executable,
        "-m",
        "PyInstaller",
        "--onefile",
        "--windowed",
        "--name=MoneyTracker",
        "main.py"
    ]
    
    result = subprocess.run(cmd, cwd=base_dir)
    
    if result.returncode == 0:
        exe_path = os.path.join(base_dir, "dist", "MoneyTracker.exe")
        
        # Check if exe was created
        if os.path.exists(exe_path):
            exe_size = os.path.getsize(exe_path) / (1024 * 1024)  # Convert to MB
            
            print("\n" + "=" * 60)
            print("[✓] Build successful!")
            print("=" * 60)
            print(f"\n📦 Executable Details:")
            print(f"  Location: {exe_path}")
            print(f"  Size: {exe_size:.1f} MB")
            print(f"\n🚀 You can now:")
            print(f"  • Run it by double-clicking MoneyTracker.exe")
            print(f"  • Move it to any folder on your PC")
            print(f"  • Create a shortcut on your desktop")
            print(f"  • Share it with others")
            print(f"\n📝 Note:")
            print(f"  Keep data.json in the same folder as MoneyTracker.exe to save entries.")
            print(f"  The .exe file is standalone and includes all dependencies.")
        else:
            print("\n[✗] Build completed but executable not found!")
            sys.exit(1)
    else:
        print("\n[✗] Build failed. Check the error messages above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
