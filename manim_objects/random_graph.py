import numpy as np
from manim import Graph, VMobject


class RandomGraph(VMobject):
    def __init__(
            self,
            num_nodes,
            connectivity_rate: float = 0.5,
            width: float = 1.0,
            height: float = 1.0,
            seed: int = 0, **kwargs
    ):
        super().__init__(**kwargs)

        vertices = [i for i in range(num_nodes)]

        # put all the possible edges in a list
        edges = []
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                edges.append((i, j))

        # shuffle the list of edges
        if seed is not None:
            np.random.seed(seed)

        np.random.shuffle(edges)

        # keep the first connectivity_rate * len(edges) edges
        num_edges = int(connectivity_rate * len(edges))
        edges = edges[:num_edges]

        # create graph
        self.graph = Graph(vertices, edges)

        self.add(self.graph)

        self.set(width=width, height=height)