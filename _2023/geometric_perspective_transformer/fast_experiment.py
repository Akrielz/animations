from manim import Write, Create, Transform

from colors.color import ColorSchemeScene
from manim_objects.random_graph import RandomGraph


class FastExperiment(ColorSchemeScene):
    def construct(self):
        graph = RandomGraph(num_nodes=20, connectivity_rate=0.3, seed=0, width=5, height=5)
        self.play(Create(graph), run_time=2.0)
        self.wait(1.0)