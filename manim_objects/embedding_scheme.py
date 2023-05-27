from manim import VMobject, Arrow, Circle, Line, Text, DOWN

from colors.color import colors_hex
from manim_objects.addition_circle import AdditionCircle
from manim_objects.positional_circle import PositionalCircle
from manim_objects.text_box import TextBox


class EmbeddingScheme(VMobject):
    def __init__(
            self,
            text: str,
            font_size: int = 24,
            line_width: float = 1.0,
            **kwargs
    ):
        super().__init__(**kwargs)

        self.line_width = line_width

        # Create main box
        self.input_embedding_box = TextBox(text, width=3.0, height=1.5, font_size=font_size)

        # Create an arrow that exits the box
        self.input_arrow = Arrow(
            start=self.input_embedding_box.get_center() + [0.0, -1.5, 0.0],
            end=self.input_embedding_box.get_center() + [0.0, -0.5, 0.0],
            color=colors_hex['white']
        )

        # Create an arrow that enters the box
        self.output_arrow = Arrow(
            start=self.input_embedding_box.get_center() + [0.0, 0.5, 0.0],
            end=self.input_embedding_box.get_center() + [0.0, 2.0, 0.0],
            color=colors_hex['white']
        )

        # Set the stroke width of the arrows
        self.input_arrow.set_stroke(width=self.line_width)
        self.output_arrow.set_stroke(width=self.line_width)

        # Create a circle at the tip of the arrow
        self.addition_circle = AdditionCircle(color=colors_hex['white'])
        self.addition_circle.move_to(self.input_embedding_box.get_center() + [0.0, 2.0, 0.0])
        self.addition_circle.scale(0.25)
        self.addition_circle.set_stroke(width=self.line_width)

        # Create the positional circle
        self.positional_circle = PositionalCircle(color=colors_hex['white'])
        self.positional_circle.move_to(self.input_embedding_box.get_center() + [-1.5, 2.0, 0.0])
        self.positional_circle.scale(0.5)
        self.positional_circle.set_stroke(width=self.line_width)

        # Add text next to the positional circle
        self.positional_text = Text('Positional\n Encoding', font_size=font_size)
        self.positional_text.set_color(colors_hex['white'])
        self.positional_text.move_to(self.positional_circle.get_center() + [-1.5, 0.0, 0.0])

        # Create line between the circles
        self.connecting_line = Line(
            start=self.addition_circle.get_center() + [-0.25, 0.0, 0.0],
            end=self.positional_circle.get_center() + [0.5, 0.0, 0.0],
        )
        self.connecting_line.set_stroke(width=self.line_width)

        # Add all the objects to the VMobject
        self.add(
            self.input_embedding_box,
            self.input_arrow,
            self.output_arrow,
            self.addition_circle,
            self.positional_circle,
            self.positional_text,
            self.connecting_line,
        )
