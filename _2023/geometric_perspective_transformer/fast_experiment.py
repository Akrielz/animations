import numpy as np
from manim import Write, Create, Transform

from colors.color import ColorSchemeScene
from manim_objects.addition_circle import AdditionCircle
from manim_objects.embedding_scheme import EmbeddingScheme
from manim_objects.multi_line import MultiLine
from manim_objects.positional_circle import PositionalCircle
from manim_objects.random_graph import RandomGraph
from manim_objects.transformer_encoder_scheme import TransformerEncoderScheme


class FastExperiment(ColorSchemeScene):
    def construct(self):
        obj = TransformerEncoderScheme()

        # Make the circle twice as big
        obj.scale(0.5)

        self.play(Create(obj), run_time=15.0)
        self.wait(5.0)
