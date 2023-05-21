import PIL


def crop_image(
        image_path: str,
        crop_width: int,
        crop_height: int,
        save_path: str = None
):
    if save_path is None:
        save_path = image_path

    image = PIL.Image.open(image_path)

    width = image.width
    height = image.height

    center = (width / 2, height / 2)
    left = center[0] - crop_width / 2
    right = center[0] + crop_width / 2
    top = center[1] - crop_height / 2
    bottom = center[1] + crop_height / 2

    image = image.crop((left, top, right, bottom))
    image.save(save_path)


crop_image("resources/img.png", 1024, 1024, "resources/img_cropped.png")