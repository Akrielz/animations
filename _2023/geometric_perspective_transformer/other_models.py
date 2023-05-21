import numpy as np
from manim import Write, ImageMobject

from colors.color import ColorSchemeScene
from manim_objects.animations import fade_in_animation
from manim_objects.random_graph import RandomGraph
from manim_objects.sound_wave import SoundWave
from manim_objects.text_box import TextBox


class OtherModelsScene(ColorSchemeScene):
    def __init__(self):
        super().__init__()
        self.center_coords = np.array([0.0, 0.0, 0.0])
        self.image_model = None
        self.sound_model = None
        self.graph_model = None

        self.image = None
        self.sound_wave = None
        self.graph = None

    def show_models(self):
        graph_model = TextBox("Graph", width=2.0, height=1.0)
        graph_model.move_to(self.center_coords + [-4.0, 0.0, 0.0])
        self.graph_model = graph_model

        image_model = TextBox("Image", width=2.0, height=1.0)
        image_model.move_to(self.center_coords)
        self.image_model = image_model

        sound_model = TextBox("Sound", width=2.0, height=1.0)
        sound_model.move_to(self.center_coords + [4.0, 0.0, 0.0])
        self.sound_model = sound_model

        self.play(Write(image_model), Write(sound_model), Write(graph_model), run_time=3.0)

    def send_inputs(self):
        # Add an image
        image = ImageMobject("resources/vincent_cropped.png")
        image.set(width=1.0, height=1.0)
        image.move_to(self.image_model.get_center() + [0.0, -2.0, 0.0])

        image_animation = fade_in_animation(image)

        # Add soundwave
        sound_wave = SoundWave(width=2.0, height=1.0, density=40, seed=2)
        sound_wave.move_to(self.sound_model.get_center() + [0.0, -2.0, 0.0])

        sound_wave_animation = Write(sound_wave)

        # Add Graph
        graph = RandomGraph(num_nodes=12, connectivity_rate=0.3, seed=0, width=1, height=1)
        graph.move_to(self.graph_model.get_center() + [0.0, -2.0, 0.0])

        graph_animation = Write(graph)

        self.play(image_animation, sound_wave_animation, graph_animation, run_time=4.0)

        self.wait(2.0)

        # Animate the image moving to the center of chat gpt rectangle
        # image_animation = image.animate
        # image_animation.move_to(self.image_model.get_center())
        # image_animation.set_opacity(0.0)
        # self.play(image_animation, run_time=2.0)

    def construct(self):
        self.show_models()
        self.send_inputs()

        # # Animate answer
        # answer_text = Text("Cat", font_size=18)
        # answer_text.move_to(self.image_model.get_center())
        # answer_text.set_opacity(0.0)
        #
        # answer_animation = answer_text.animate
        # answer_animation.move_to(self.image_model.get_center() + [0.0, 2.0, 0.0])
        # answer_animation.set_opacity(1.0)
        # self.play(answer_animation, run_time=2.0)