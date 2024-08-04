# Implement Caesar Cipher

# Create a Python program that can encrypt and decrypt text using the Caesar Cipher algorithm. Allow users to input a message and a shift value to perform encryption and decryption.


def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            encrypted_text += chr(start + (ord(char) - start + shift_amount) % 26)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                start = ord('a')
            else:
                start = ord('A')
            decrypted_text += chr(start + (ord(char) - start - shift_amount) % 26)
        else:
            decrypted_text += char
    return decrypted_text

def print_menu():
    print("\n=======================")
    print("  Caesar Cipher Tool")
    print("=======================")
    print("1. Encrypt a message")
    print("2. Decrypt a message")
    print("3. Exit")
    print("=======================")

def main():
    while True:
        print_menu()
        choice = input("Choose an option (1, 2, or 3): ").strip()
        
        if choice == '1':
            message = input("Enter your message to encrypt: ")
            if any(char.isdigit() for char in message):
                print("Error: Message should not contain numbers.")
                continue
            while True:
                try:
                    shift = int(input("Enter the shift value (integer): "))
                    break
                except ValueError:
                    print("Invalid shift value. Please enter an integer.")
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"\nEncrypted message: {encrypted_message}")

        elif choice == '2':
            message = input("Enter your message to decrypt: ")
            if any(char.isdigit() for char in message):
                print("Error: Message should not contain numbers.")
                continue
            while True:
                try:
                    shift = int(input("Enter the shift value (integer): "))
                    break
                except ValueError:
                    print("Invalid shift value. Please enter an integer.")
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"\nDecrypted message: {decrypted_message}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
