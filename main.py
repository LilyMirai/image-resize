import os
import sys
from PIL import Image
import argparse
import subprocess

print("Python executable:", sys.executable)
print("Python version:", sys.version)

def confirm_image_size(image_path):
    """Check if the image size is less than half of A4 300dpi and confirm with the user."""
    A4_300DPI = (2480, 3508)  # A4 dimensions in pixels at 300dpi
    HALF_A4 = (A4_300DPI[0] // 2, A4_300DPI[1] // 2)

    with Image.open(image_path) as img:
        if img.size[0] < HALF_A4[0] or img.size[1] < HALF_A4[1]:
            print(f"Warning: The image size is smaller than half of A4 300dpi ({HALF_A4}).")
            response = input("Are you sure this is the correct file? (y/n): ").strip().lower()
            if response != 'y':
                print("Exiting.")
                sys.exit(1)

def confirm_image_format(image_path):
    """Ensure the input image is in PNG format."""
    if not image_path.lower().endswith(".png"):
        print("Error: The input file must be a PNG image.")
        sys.exit(1)

def process_twitter(image_path):
    """Create a PNG image half the size optimized for Twitter."""
    with Image.open(image_path) as img:
        new_size = (img.size[0] // 2, img.size[1] // 2)
        img = img.resize(new_size, Image.LANCZOS)
        output_path = os.path.splitext(image_path)[0] + " - Twitter Public.png"
        img.save(output_path, format="PNG", optimize=True)
        print(f"Twitter-optimized image saved as: {output_path}")

def process_instagram(image_path):
    """Create a JPEG image half the size optimized for Instagram."""
    with Image.open(image_path) as img:
        new_size = (img.size[0] // 2, img.size[1] // 2)
        img = img.resize(new_size, Image.LANCZOS)
        if img.mode == "RGBA":
            img = img.convert("RGB")  # Convert to RGB mode to remove alpha channel
        output_path = os.path.splitext(image_path)[0] + " - Instagram Public.jpg"
        img.save(output_path, format="JPEG", quality=85, optimize=True)
        print(f"Instagram-optimized image saved as: {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Image processing application.")
    parser.add_argument("image", nargs="?", help="Path to the input PNG image.")
    parser.add_argument("--twitter", action="store_true", help="Process image for Twitter.")
    parser.add_argument("--instagram", action="store_true", help="Process image for Instagram.")
    args = parser.parse_args()

    if args.image:
        confirm_image_format(args.image)
        confirm_image_size(args.image)
        if args.twitter:
            process_twitter(args.image)
        if args.instagram:
            process_instagram(args.image)
        if not args.twitter and not args.instagram:
            process_twitter(args.image)
            process_instagram(args.image)
    else:
        # Interactive menu for image processing
        image_path = input("Enter the path to the PNG image: ").strip()
        confirm_image_format(image_path)
        confirm_image_size(image_path)
        while True:
            print("Select processing options:")
            print("1. Twitter")
            print("2. Instagram")
            print("3. Both")
            choice = input("Enter your choice (1/2/3): ").strip()
            if choice == "1":
                process_twitter(image_path)
                break
            elif choice == "2":
                process_instagram(image_path)
                break
            elif choice == "3":
                process_twitter(image_path)
                process_instagram(image_path)
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()