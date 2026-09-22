#!/usr/bin/env python3
"""
ghadah_test - A simple test script
"""

def greet(name: str) -> str:
    """Return a greeting message."""
    return f"Hello, {name}!"

def main():
    print(greet("World"))
    print("HCE Test successful!")

if __name__ == "__main__":
    main()