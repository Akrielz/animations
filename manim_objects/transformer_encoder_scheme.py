from manim import VMobject, Arrow, Line

from manim_objects.embedding_scheme import EmbeddingScheme
from manim_objects.multi_line import MultiLine
from manim_objects.text_box import TextBox


class TransformerEncoderScheme(VMobject):
    def __init__(
            self,
            font_size: int = 24,
            line_width: float = 2.0,
            **kwargs
    ):
        super().__init__(**kwargs)

        self.line_width = line_width

        self.embedding_scheme = EmbeddingScheme(font_size=font_size, line_width=line_width, text="Input Embedding")
        self.embedding_scheme.move_to([0.0, -4.0, 0.0])

        self.multi_head_attention = TextBox("Multi-Head \n Attention", width=3.0, height=1.5, font_size=font_size)
        self.multi_head_attention.move_to(self.embedding_scheme.addition_circle.get_center() + [0.0, 2.75, 0.0])

        self.residual_1 = TextBox("Add & Norm", width=3.0, height=1.0, font_size=font_size)
        self.residual_1.move_to(self.multi_head_attention.get_center() + [0.0, 1.5, 0.0])

        self.feed_forward = TextBox("Feed Forward", width=3.0, height=1.5, font_size=font_size)
        self.feed_forward.move_to(self.residual_1.get_center() + [0.0, +2.5, 0.0])

        self.residual_2 = TextBox("Add & Norm", width=3.0, height=1.0, font_size=font_size)
        self.residual_2.move_to(self.feed_forward.get_center() + [0.0, +1.5, 0.0])

        # Draw arrows
        self.input_middle_arrow = Arrow(
            start=self.multi_head_attention.get_center() + [0.0, -2.5, 0.0],
            end=self.multi_head_attention.get_center() + [0.0, -0.75, 0.0],
            buff=0.0,
        )
        self.input_middle_arrow.set_stroke(width=self.line_width)

        self.input_left_arrow = MultiLine(
            [
                self.input_middle_arrow.get_center(),
                self.input_middle_arrow.get_center() + [-1.0, 0.0, 0.0],
                self.input_middle_arrow.get_center() + [-1.0, 0.75, 0.0],
            ],
            is_arrow=True,
        )
        self.input_left_arrow.set_stroke(width=self.line_width)

        self.input_right_arrow = MultiLine(
            [
                self.input_middle_arrow.get_center(),
                self.input_middle_arrow.get_center() + [1.0, 0.0, 0.0],
                self.input_middle_arrow.get_center() + [1.0, 0.75, 0.0],
            ],
            is_arrow=True,
        )
        self.input_right_arrow.set_stroke(width=self.line_width)

        self.residual_arrow_1 = MultiLine(
            [
                self.input_middle_arrow.get_center() + [0.0, -0.25, 0.0],
                self.input_middle_arrow.get_center() + [-3.0, -0.25, 0.0],
                [self.input_middle_arrow.get_center()[0] - 3.0, self.residual_1.get_center()[1], 0.0],
                self.residual_1.get_center() + [-1.5, 0.0, 0.0],
            ],
            is_arrow=True,
        )
        self.residual_arrow_1.set_stroke(width=self.line_width)

        self.mha_to_residual_line = Line(
            start=self.multi_head_attention.get_center() + [0.0, 0.75, 0.0],
            end=self.residual_1.get_center() + [0.0, -0.5, 0.0],
        )
        self.mha_to_residual_line.set_stroke(width=self.line_width)

        self.norm_to_ff_arrow = Arrow(
            start=self.residual_1.get_center() + [0.0, 0.5, 0.0],
            end=self.feed_forward.get_center() + [0.0, -0.75, 0.0],
            buff=0.0,
        )
        self.norm_to_ff_arrow.set_stroke(width=self.line_width)

        self.residual_arrow_2 = MultiLine(
            [
                self.norm_to_ff_arrow.get_center(),
                self.norm_to_ff_arrow.get_center() + [-3.0, 0.0, 0.0],
                [self.norm_to_ff_arrow.get_center()[0] - 3.0, self.residual_2.get_center()[1], 0.0],
                self.residual_2.get_center() + [-1.5, 0.0, 0.0],
            ],
            is_arrow=True,
        )
        self.residual_arrow_2.set_stroke(width=self.line_width)

        self.ff_to_norm_line = Line(
            start=self.feed_forward.get_center() + [0.0, 0.75, 0.0],
            end=self.residual_2.get_center() + [0.0, -0.5, 0.0],
        )
        self.ff_to_norm_line.set_stroke(width=self.line_width)

        self.add(self.embedding_scheme)

        self.add(self.input_middle_arrow)
        self.add(self.input_left_arrow)
        self.add(self.input_right_arrow)
        self.add(self.multi_head_attention)
        self.add(self.residual_arrow_1)
        self.add(self.mha_to_residual_line)
        self.add(self.residual_1)

        self.add(self.norm_to_ff_arrow)
        self.add(self.feed_forward)
        self.add(self.residual_arrow_2)
        self.add(self.ff_to_norm_line)
        self.add(self.residual_2)