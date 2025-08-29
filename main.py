#!/usr/bin/env python3
"""
Main entry point for the Hospital Management System
"""
import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from app.cli import HospitalCLI

def main():
    """Main function to run the CLI"""
    cli = HospitalCLI()
    print("Welcome to Hospital Management System!")
    cli.main_menu()

if __name__ == "__main__":
    main()