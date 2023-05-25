from manim import VMobject, Circle, Line


class AdditionCircle(VMobject):
    def __init__(
            self,
            color: str = "#FFFFFF",
            line_off_set: float = 0.8
    ):
        super().__init__()

        # add a circle
        self.circle = Circle(color=color)

        # Add two lines to the circle
        self.vertical_line = Line(
            start=[0.0, -line_off_set, 0.0],
            end=[0.0, line_off_set, 0.0],
            color=color
        )
        self.horizontal_line = Line(
            start=[-line_off_set, 0.0, 0.0],
            end=[line_off_set, 0.0, 0.0],
            color=color
        )

        # Add the circle and the lines to the VMobject
        self.add(self.circle, self.vertical_line, self.horizontal_line)