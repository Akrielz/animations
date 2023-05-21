from typing import Optional
from manim import Text, Rectangle, VGroup

from colors.color import colors_hex


class TextBox(VGroup):
    def __init__(self, text: str, width: float, height: float, font_size: Optional[int] = None):
        super().__init__()

        self.rectangle = Rectangle(width=width, height=height)
        self.rectangle.set_fill(colors_hex['light_gray'], opacity=1.0)
        self.rectangle.set_stroke(colors_hex['dark_gray'])

        if font_size is None:
            font_size = 18

        self.text = Text(text, font_size=font_size)
        self.text.set_color(colors_hex['white'])
        self.text.move_to(self)

        self.add(self.rectangle, self.text)