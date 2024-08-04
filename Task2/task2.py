# Pixel Manipulation for Image Encryption

# Develop a simple image encryption tool using pixel manipulation. You can perform operations like swapping pixel values or applying a basic mathematical operation to each pixel. Allow users to encrypt and decrypt images.

from PIL import Image
import numpy as np

def shuffle_pixels(image_data, key):
    np.random.seed(key % (2**32 - 1)) 
    shuffled_indices = np.random.permutation(image_data.size)
    return image_data.flatten()[shuffled_indices].reshape(image_data.shape)

def encrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image_data = np.array(image)
    
   
    red_channel = image_data[:,:,0]
    green_channel = image_data[:,:,1]
    blue_channel = image_data[:,:,2]
    
    # Shuffle pixels in each channel
    encrypted_red = shuffle_pixels(red_channel, key)
    encrypted_green = shuffle_pixels(green_channel, key + 1)  # Different key for green channel
    encrypted_blue = shuffle_pixels(blue_channel, key + 2)   # Different key for blue channel
    
    # Combine encrypted channels
    encrypted_data = np.stack((encrypted_red, encrypted_green, encrypted_blue), axis=-1).astype(np.uint8)
    
    encrypted_image = Image.fromarray(encrypted_data)
    encrypted_image.save(output_path)
    print(f"Encrypted image saved to {output_path}")

def decrypt_image(input_path, output_path, key):
    image = Image.open(input_path)
    image_data = np.array(image)
    
    # Separate RGB channels
    red_channel = image_data[:,:,0]
    green_channel = image_data[:,:,1]
    blue_channel = image_data[:,:,2]
    
    # Reverse shuffling in each channel
    decrypted_red = reverse_shuffle_pixels(red_channel, key)
    decrypted_green = reverse_shuffle_pixels(green_channel, key + 1)  # Use the same keys for decryption
    decrypted_blue = reverse_shuffle_pixels(blue_channel, key + 2)
    
    # Combine decrypted channels
    decrypted_data = np.stack((decrypted_red, decrypted_green, decrypted_blue), axis=-1).astype(np.uint8)
    
    decrypted_image = Image.fromarray(decrypted_data)
    decrypted_image.save(output_path)
    print(f"Decrypted image saved to {output_path}")

def reverse_shuffle_pixels(shuffled_data, key):
    np.random.seed(key % (2**32 - 1))  # Use modulo to keep key within acceptable range
    unshuffled_indices = np.argsort(np.random.permutation(shuffled_data.size))
    return shuffled_data.flatten()[unshuffled_indices].reshape(shuffled_data.shape)

def main():
    import argparse

    print("Welcome to Image Encryption and Decryption Program!")
    print("Choose an option:")
    print("1. Encrypt an image")
    print("2. Decrypt an image")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice not in ['1', '2']:
        print("Invalid choice. Please choose 1 or 2.")
        return
    
    input_path = input("Enter the path to the input image file: ")
    output_path = input("Enter the path to save the output image file: ")
    key_str = input("Enter the encryption/decryption key: ")
    
    try:
        key = int(key_str)  # Convert input string to integer
    except ValueError:
        print("Invalid key. Please enter a valid integer.")
        return
    
    if len(key_str) <=0 and len(key_str) > 10:
        print("Invalid Key")
        return
    
    if choice == '1':
        encrypt_image(input_path, output_path, key)
    elif choice == '2':
        decrypt_image(input_path, output_path, key)

if __name__ == "__main__":
    main()
