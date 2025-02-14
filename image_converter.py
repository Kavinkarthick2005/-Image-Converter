from PIL import Image
import sys

def convert_image(input_path, output_format):
    img = Image.open(input_path)
    output_path = f"{input_path.rsplit('.', 1)[0]}.{output_format}"
    img.save(output_path)
    print(f"Image saved as {output_path}")

if __name__ == "__main__":
    input_path = input("Enter image path: ")
    output_format = input("Enter output format (jpg, png, bmp): ")
    convert_image(input_path, output_format)
