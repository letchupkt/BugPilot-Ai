#!/usr/bin/env python3
"""
BugPilot AI Installation Helper
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages"""
    print("🔧 Installing BugPilot AI Requirements...")
    
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Requirements installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install requirements")
        return False

def main():
    print("🐛 BugPilot AI - Installation Helper")
    print("=" * 40)
    
    if not os.path.exists("requirements.txt"):
        print("❌ requirements.txt not found!")
        return
    
    if install_requirements():
        print("🎉 Installation Complete!")
        print("To run BugPilot AI:")
        print("  python bugpilot_ai.py")
        print("To run Kali Server:")
        print("  python kali_server.py")
    else:
        print("❌ Installation failed. Please install requirements manually:")
        print("  pip install -r requirements.txt")

if __name__ == "__main__":
    main()
