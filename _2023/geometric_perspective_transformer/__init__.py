from manim import Scene

from _2023.geometric_perspective_transformer.chat_gpt import ChatGPTScene
from _2023.geometric_perspective_transformer.other_models import OtherModelsScene


class AllScenes(Scene):
    def __init__(self):
        __init__ = super().__init__()

        chat_gpt_scene = ChatGPTScene()
        other_models_scene = OtherModelsScene()

        self.scenes = [chat_gpt_scene, other_models_scene]

    def construct(self):
        for scene in self.scenes:
            scene.construct()