#!/usr/bin/python3
"""
Determines if a given data set is a valid UTF-8 encoding.

The function iterates over each byte in the data set and checks if it conforms
to the UTF-8 encoding rules. It verifies whether each byte is a valid UTF-8
character representation, ensuring that the data adheres to the UTF-8
specification regarding byte order and format. Continuation bytes (10xxxxxx)
are validated following the leading byte.

If any byte violates the UTF-8 encoding rules, the function returns False.
Otherwise, it returns True, indicating that the entire data set is a valid
UTF-8 encoding.
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
    for byte in data:
        # Check if the byte is in the format 10xxxxxx (continuation byte)
        if byte & 0b11000000 == 0b10000000:
            continue
        # Count the number of leading set bits
        leading_set_bits = 0
        mask = 0b10000000
        while byte & mask:
            leading_set_bits += 1
            mask >>= 1
        # A character in UTF-8 can be 1 to 4 bytes long
        if leading_set_bits == 1 or leading_set_bits > 4:
            return False
        # Check continuation bytes (10xxxxxx)
        for _ in range(leading_set_bits - 1):
            byte >>= 1
            if byte & 0b10000000 == 0 or byte & 0b01000000:
                return False
    return True
