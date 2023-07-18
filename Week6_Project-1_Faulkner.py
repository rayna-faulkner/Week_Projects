plaintext = input("Enter the plaintext: ")
distance = int(input("Enter the distance: "))

encrypted_text = ""
for char in plaintext:
    if char.isprintable():
        lowest_printable_char = ord(' ')
        encrypted_char = chr((ord(char) - lowest_printable_char + distance) % 95 + lowest_printable_char)
        encrypted_text += encrypted_char
    else:
        encrypted_text += char

print("Encrypted text:", encrypted_text)
