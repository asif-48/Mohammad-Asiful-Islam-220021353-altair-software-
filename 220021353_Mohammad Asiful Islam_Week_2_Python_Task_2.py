from PIL import Image, ImageEnhance, ImageFilter
import os

def filters(image_path, output_dir):
    original_image = Image.open(image_path)
    image_name, image_ext = os.path.splitext(os.path.basename(image_path))
    filters = [
        ("grayscale", lambda img: img.convert("L")),
        ("blur", lambda img: img.filter(ImageFilter.BLUR)),
        ("brightness", lambda img: ImageEnhance.Brightness(img).enhance(1.5)),
        ("inversion", lambda img: ImageEnhance.Color(img).enhance(-1)),
        ("contrast", lambda img: ImageEnhance.Contrast(img).enhance(1.5)),
        ("erosion", lambda img: img.filter(ImageFilter.MinFilter(size=3))),
    ]
os.makedirs(output_dir, exist_ok=True)
    for filter_name, filter_func in filters:
        filtered_image = filter_func(original_image.copy())
        output_path = os.path.join(output_dir, f"{image_name}-{filter_name}{image_ext}")
        filtered_image.save(output_path)
        print(f"Saved filtered image: {output_path}")
if __name__ == "__main__":
#we have to apply our custom file paths here   
    input_image_path = r"E:\Downloads\download.jpeg"
    output_directory = r"E:\Downloads\Output"
    apply_filters(input_image_path, output_directory)
