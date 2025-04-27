def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = ord('A') if char.isupper() else ord('a')
            # Encrypt the character and wrap around using modulo
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Non-alphabetic characters are not changed
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Decrypting is just encrypting with a negative shift

def main():
    print("Caesar Cipher Program")
    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    encrypted_message = caesar_cipher_encrypt(message, shift)
    print(f"Encrypted Message: {encrypted_message}")

    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift)
    print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
    