import numpy as np
from manim import Write, ImageMobject, VGroup, VMobject, Text, Transform

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
        graph = RandomGraph(num_nodes=12, connectivity_rate=0.3, seed=0, width=1.0, height=1.0)
        graph.move_to(self.graph_model.get_center() + [0.0, -2.0, 0.0])

        graph_animation = Write(graph)

        self.play(image_animation, sound_wave_animation, graph_animation, run_time=4.0)

        # Animate the image moving to the center of chat gpt rectangle
        def send_input_to_model_animation(obj: VMobject, model: VMobject):
            object_animation = obj.animate
            object_animation.move_to(model.get_center())
            object_animation.set_opacity(0.0)
            return object_animation

        image_animation = send_input_to_model_animation(image, self.image_model)

        sound_wave_target = SoundWave(width=2.0, height=1.0, density=40, seed=3)
        sound_wave_target.move_to(self.sound_model.get_center())
        sound_wave_target.set_opacity(0.0)
        sound_wave_animation = Transform(sound_wave, sound_wave_target)

        graph_animation = send_input_to_model_animation(graph, self.graph_model)

        self.play(image_animation, sound_wave_animation, graph_animation, run_time=2.0)

    def send_outputs(self):
        texts = ["Shortest Route: 52km", "Cat", "You shalt not pass!"]

        def create_output_animation(text: str, model: VMobject):
            answer_text = Text(text, font_size=18)
            answer_text.move_to(model.get_center())
            answer_text.set_opacity(0.0)

            answer_animation = answer_text.animate
            answer_animation.move_to(model.get_center() + [0.0, 2.0, 0.0])
            answer_animation.set_opacity(1.0)
            return answer_animation

        image_animation = create_output_animation(texts[0], self.graph_model)
        sound_wave_animation = create_output_animation(texts[1], self.image_model)
        graph_animation = create_output_animation(texts[2], self.sound_model)

        self.play(image_animation, sound_wave_animation, graph_animation, run_time=2.0)

    def construct(self):
        self.show_models()
        self.send_inputs()
        self.send_outputs()
