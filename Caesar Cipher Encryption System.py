import os
import string
import time

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def encrypt(message, shift):
    alphabet = string.ascii_lowercase
    encrypted_message = ""

    for letter in message:
        if letter.lower() in alphabet:
            original_position = alphabet.index(letter.lower())
            new_position = (original_position + shift) % 26
            encrypted_letter = alphabet[new_position]

            if letter.isupper():
                encrypted_letter = encrypted_letter.upper()

            encrypted_message += encrypted_letter
        else:
            encrypted_message += letter
    return encrypted_message

def decrypt(message, shift):
    return encrypt(message, -shift)


while True:
    clear_screen()
    print("\n=== Caesar Cipher Program ===\n")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit\n")

    choice = input("Enter your choice: ")

    if choice == '1':
        clear_screen()
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter shift number: "))
        encrypted = encrypt(message, shift)
        print("\nEncrypted message:", encrypted)
        input("\nPress Enter to continue...")

    elif choice == '2':
        clear_screen()
        message = input("Enter the message to decrypt: ")
        shift = int(input("Enter shift number: "))
        decrypted = decrypt(message, shift)
        print("\nDecrypted message:", decrypted)
        input("\nPress Enter to continue...")

    elif choice == '3':
        print("Exiting program...")
        time.sleep(2)
        break

    else:
        print("Invalid choice! Try again.")
        time.sleep(2)
