from typing import List

from manim import Scene


def rgb_to_hex(rgb: List[int]):
    return "#" + "".join(f"{x:02x}" for x in rgb)


colors = {
    "gray": [52, 53, 65],
    "light_gray": [64, 65, 79],
    "dark_gray": [32, 33, 35],
    "white": [255, 255, 255],
}

colors_hex = {
    color: rgb_to_hex(rgb) for color, rgb in colors.items()
}


class ColorSchemeScene(Scene):
    def __init__(self):
        super().__init__()
        self.camera.background_color = colors_hex["gray"]