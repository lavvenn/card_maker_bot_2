from PIL import Image, ImageDraw


def crop_to_square(image: Image.Image) -> Image.Image:
    width, height = image.size
    min_side = min(width, height)

    left = (width - min_side) // 2
    top = (height - min_side) // 2
    right = left + min_side
    bottom = top + min_side

    return image.crop((left, top, right, bottom))


def make_circle_avatar(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    image = crop_to_square(image)
    image = image.resize(size, Image.LANCZOS).convert("RGBA")

    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size[0], size[1]), fill=255)

    result = Image.new("RGBA", size)
    result.paste(image, (0, 0), mask)

    return result
