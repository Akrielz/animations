from typing import Optional

import numpy as np
from manim import VGroup, Line, Transform

from colors.color import colors_hex


class SoundWave(VGroup):
    def __init__(self, width: float, height: float, density: int = 10, seed: Optional[int] = None):
        super().__init__()
        self.width = width
        self.height = height
        self.density = density

        left = self.get_center()[0] - width / 2
        right = self.get_center()[0] + width / 2

        if seed is not None:
            np.random.seed(seed)

        noise = np.random.uniform(low=0.1, high=height, size=density)
        self.noise = noise

        lines = []
        for i in range(density):
            x = left + i * (right - left) / density
            bot = self.get_center()[1] - noise[i] / 2
            top = self.get_center()[1] + noise[i] / 2

            line = Line(start=[x, bot, 0.0], end=[x, top, 0.0])
            line.set_stroke(color=colors_hex['white'], width=width)
            lines.append(line)

        self.lines = lines
        self.add(*lines)

    def noise_animation(self, seed: Optional[int] = None):
        if seed is not None:
            np.random.seed(seed)

        new_soundwave = SoundWave(width=self.width, height=self.height, density=self.density, seed=seed)
        animation = Transform(self, new_soundwave)

        self = new_soundwave
        return animation
