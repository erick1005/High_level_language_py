 code is AI-generated. Review and use carefully. Visit our FAQ for more information.

# Define the alphabet of base 58
alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"

# Define a function that converts a number to base 58
def to_base58(num):
    # Initialize an empty string to store the result
    result = ""
    # If the number is negative, make it positive and remember the sign
    sign = "-" if num < 0 else ""
    num = abs(num)
    # Repeat until the number becomes zero
    while num > 0:
        # Divide the number by 58 and get the remainder
        num, remainder = divmod(num, 58)
        # Convert the remainder to a character using the alphabet
        char = alphabet[remainder]
        # Append the character to the result
        result = char + result
    # Return the result with the sign if any
    return sign + result