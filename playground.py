from PIL import Image

def crop_center(image: Image.Image, size: tuple[int, int]):
    width, height = image.size   # Get dimensions

    left = (width - size[0])/2
    top = (height - size[1])/2
    right = (width + size[0])/2
    bottom = (height + size[1])/2

    # Crop the center of the image
    return image.crop((left, top, right, bottom))



image = Image.open("./cat.png")
cropped_image = crop_center(image, (512, 512))

cropped_image.save("./cat_cropped.png")