#!/usr/bin/env python3

# Main entry point for the Hospital Management System

import sys
import os

# Add the current directory to Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

#import cli interface code
from app.cli import HospitalCLI

def main():
    #function that runs the cli code
    cli = HospitalCLI()
    print("Welcome to Hospital Management System!")
    cli.main_menu()

if __name__ == "__main__":
    main()