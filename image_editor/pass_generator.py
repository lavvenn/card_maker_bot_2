from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from .utils import make_circle_avatar


class PassGenirator:

    def __init__(self):
        self.tmplate_path = "templates/temolate.png"
        self.font_path = "templates/Evolventa-Regular.ttf"

    def genirate(
        self,
        firstname: str,
        lastname: str,
        photo_path: Path,
        output_path: Path,
    ):
        template = Image.open(self.tmplate_path)
        photo = Image.open(photo_path)
        photo = make_circle_avatar(photo, (100, 100))

        template.paste(photo, (100, 200), photo)

        draw = ImageDraw.Draw(template)
        font = ImageFont.truetype(self.font_path, size=40)

        draw.text((500, 250), lastname, font=font)
        draw.text((500, 350), firstname, font=font)

        output_path.parent.mkdir(parents=True, exist_ok=True)

        template.save(output_path)

        return output_path
