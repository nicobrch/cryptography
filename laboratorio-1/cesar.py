#!/usr/bin/env python3

import argparse

def caesar_cipher(text, shift):
    """
    Encode the given text using the Caesar cipher algorithm with the given shift value.
    """
    result = ""
    for char in text:
        if char.isalpha():
            # Shift the character by the specified amount
            shifted_char = chr((ord(char.lower()) - ord('a') + shift) % 26 + ord('a'))
            if char.isupper():
                shifted_char = shifted_char.upper()
            result += shifted_char
        else:
            result += char
    return result

if __name__ == "__main__":
    # Parse the command line arguments
    parser = argparse.ArgumentParser(description="Encode text using the Caesar cipher algorithm.")
    parser.add_argument("text", help="the text to encode")
    parser.add_argument("shift", type=int, help="the amount to shift each character by")
    args = parser.parse_args()

    # Encode the text using the Caesar cipher algorithm
    encoded_text = caesar_cipher(args.text, args.shift)
    print(encoded_text)
