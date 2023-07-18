def caesar_cipher_decrypt(encrypted_text, distance):
    plaintext = ""
    for char in encrypted_text:
        if char.isprintable():
            encrypted_txt = ord(' ')
            decrypted_char = chr((ord(char) - encrypted_txt - distance) % 95 + encrypted_txt)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext


encrypted_text = input("Enter the encrypted text: ")
distance = int(input("Enter the distance: "))

plaintext = caesar_cipher_decrypt(encrypted_text, distance)
print("Plaintext:", plaintext)
