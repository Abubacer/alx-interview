#!/usr/bin/python3
"""
Determines if a given data set is a valid UTF-8 encoding.

The function ensures that each byte in the data list follows the rules
of UTF-8 encoding, including correct multi-byte character sequences.
It returns True if all characters are properly encoded and False otherwise.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding

        Args:
            data (list): A list of ints representing bytes in the data set.

        Returns:
            bool: True if the data set is a valid UTF-8 encoding
                  False otherwise.
    """
    bytes_remaining = 0
    for byte in data:
        # Keep only the 8 least significant bits
        byte %= 256
        if bytes_remaining == 0:
            if byte >> 7 == 0b0:
                # Single-byte character, move to the next byte
                continue
            # Two-byte character (110xxxxx 10xxxxxx)
            if byte >> 5 == 0b110:
                bytes_remaining = 1
            # Three-byte character (1110xxxx 10xxxxxx 10xxxxxx)
            elif byte >> 4 == 0b1110:
                bytes_remaining = 2
            # Four-byte character
            elif byte >> 3 == 0b11110:
                bytes_remaining = 3
            else:
                return False
        else:
            # Check if the byte is a continuation byte
            if byte >> 6 != 0b10:
                return False
            # Decrement the number of bytes remaining for the character
            bytes_remaining -= 1

    return bytes_remaining == 0
