import numpy as np
from manim import VMobject, Circle, FunctionGraph


class PositionalCircle(VMobject):
    def __init__(
            self,
            color: str = "#FFFFFF",
            **kwargs
    ):
        super().__init__(**kwargs)

        # add a circle
        self.circle = Circle(color=color)

        # Add a sinus line from left to right
        self.sinus_graph = FunctionGraph(
            lambda x: 2 * np.sin(x / 2),
            color=color,
        )
        self.sinus_graph.set_width(self.circle.get_width())

        # Add the circle and the lines to the VMobject
        self.add(self.circle, self.sinus_graph)