def caesar_cipher(text, shift, mode='encrypt'):
    result = ""

    # Adjust shift based on mode
    if mode == 'decrypt':
        shift = -shift

    # Loop through each character in the text
    for char in text:
        # Check if character is uppercase or lowercase and shift accordingly
        if char.isalpha():
            # Preserve the case of the character
            ascii_offset = 65 if char.isupper() else 97
            shifted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += shifted_char
        else:
            # Add character as-is if it's not alphabetical (e.g., punctuation)
            result += char

    return result


def main():
    # User input for message and shift value
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (a positive integer): "))
    action = input("Would you like to encrypt or decrypt the message? (enter 'encrypt' or 'decrypt'): ").strip().lower()

    # Encryption or decryption based on user's choice
    if action == 'encrypt':
        encrypted_message = caesar_cipher(message, shift, mode='encrypt')
        print(f"Encrypted message: {encrypted_message}")
    elif action == 'decrypt':
        decrypted_message = caesar_cipher(message, shift, mode='decrypt')
        print(f"Decrypted message: {decrypted_message}")
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
