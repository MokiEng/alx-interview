#!/usr/bin/python3
"""UTF-8 Validation's module"""


def validUTF8(data):
    """Initialize a variable to keep track of
    the number of valid leading bytes.
    """
    valid_leading_bytes = 0
    for byte in data:
        if byte >> 6 == 0b10:
            valid_leading_bytes -= 1
            if valid_leading_bytes < 0:
                return False
        else:
            if valid_leading_bytes > 0:
                return False
            if byte >> 7 == 0:
                valid_leading_bytes = 0
            elif byte >> 5 == 0b110:
                valid_leading_bytes = 1
            elif byte >> 4 == 0b1110:
                valid_leading_bytes = 2
            elif byte >> 3 == 0b11110:
                valid_leading_bytes = 3
            else:
                return False

    return valid_leading_bytes == 0
