from PIL import Image

def encrypt_decrypt_image(input_file, key, mode):
    try:
        # Open the image file
        img = Image.open(input_file)
        img = img.convert("RGBA")  
        pixels = img.load()

        width, height = img.size

        for x in range(width):
            for y in range(height):
                r, g, b, a = pixels[x, y]

                if mode == 'e':
                    r = r ^ key
                    g = g ^ key
                    b = b ^ key
                elif mode == 'd':
                    r = r ^ key
                    g = g ^ key
                    b = b ^ key

                pixels[x, y] = (r, g, b, a)

        output_file = "output_encrypted.png" if mode == 'e' else "output_decrypted.png"
        img.save(output_file)
        print(f"\n✅ Successfully {'encrypted' if mode == 'e' else 'decrypted'} the image.")
        print(f" Output saved as: {output_file}")

    except FileNotFoundError:
        print(" Error: File not found. Please check the filename.")
    except Exception as e:
        print(" Error:", e)

def main():
    print("=== Image Encryption Tool ===")

    input_file = input("Enter input image file name (e.g., input.png): ").strip()
    
    try:
        key = int(input("Enter numeric key (e.g., 123): "))
    except ValueError:
        print(" Invalid key. Please enter an integer.")
        return

    mode = input("Encrypt or Decrypt? (E/D): ").strip().lower()

    if mode not in ['e', 'd']:
        print(" Invalid mode. Choose 'E' or 'D'.")
        return

    encrypt_decrypt_image(input_file, key, mode)

if __name__ == "__main__":
    main()
