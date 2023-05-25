from manim import VMobject, Arrow

from manim_objects.text_box import TextBox


class TransformerEncoderScheme(VMobject):
    def __init__(self, font_size: int = 24, **kwargs):
        super().__init__(**kwargs)

        self.multi_head_attention = TextBox("Multi-Head \n Attention", width=3.0, height=1.5, font_size=font_size)
        self.multi_head_attention.move_to([0.0, -3.0, 0.0])

        self.residual_1 = TextBox("Add & Norm", width=3.0, height=1.0, font_size=font_size)
        self.residual_1.move_to(self.multi_head_attention.get_center() + [0.0, 1.5, 0.0])

        self.feed_forward = TextBox("Feed Forward", width=3.0, height=1.5, font_size=font_size)
        self.feed_forward.move_to(self.residual_1.get_center() + [0.0, +2.5, 0.0])

        self.residual_2 = TextBox("Add & Norm", width=3.0, height=1.0, font_size=font_size)
        self.residual_2.move_to(self.feed_forward.get_center() + [0.0, +1.5, 0.0])

        # Draw arrows
        self.input_arrow = Arrow(
            start=self.multi_head_attention.get_center() + [0.0, -1.5, 0.0],
            end=self.multi_head_attention.get_center() + [0.0, -0.5, 0.0],
        )

        self.add(self.multi_head_attention, self.residual_1, self.feed_forward, self.residual_2, self.input_arrow)
