from typing import List

import numpy as np
from manim import VMobject, Line, Arrow


class MultiLine(VMobject):
    def __init__(
            self,
            coords: np.ndarray | List[List[float]],
            is_arrow: bool = False,
            stroke_width: float = 1.0,
            max_tip_length_to_length_ratio: float = 0.25,
            **kwargs
    ):
        super().__init__(**kwargs)

        self.coords = coords
        self.is_arrow = is_arrow

        self.lines = []
        for i in range(len(coords) - 1):
            if is_arrow and i == len(coords) - 2:
                self.lines.append(
                    Arrow(
                        start=coords[i],
                        end=coords[i + 1],
                        buff=0.0,
                        max_tip_length_to_length_ratio=max_tip_length_to_length_ratio
                    )
                )
                continue

            self.lines.append(Line(start=coords[i], end=coords[i + 1]))

        for line in self.lines:
            line.set_stroke(width=stroke_width)

        self.add(*self.lines)