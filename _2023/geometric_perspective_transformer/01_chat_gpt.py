from manim import Text, Write

from colors.color import colors_hex, ColorSchemeScene
from manim_objects.text_box import TextBox


class ChatGPTScene(ColorSchemeScene):
    def construct(self):
        # Draw a square
        chat_gpt_text_box = TextBox("Chat GPT", width=4.0, height=2.0)
        self.play(Write(chat_gpt_text_box), run_time=3.0)

        # Draw text bellow the chat gpt rectangle
        question_text = Text("How to make Hot Chocolate?", font_size=18)
        question_text.set_color(colors_hex['white'])
        question_text.move_to(chat_gpt_text_box.get_center() + [0.0, -2.0, 0.0])
        self.play(Write(question_text))

        # Animate the text moving to the center of chat gpt rectangle
        question_animation = question_text.animate
        question_animation.move_to(chat_gpt_text_box.get_center())
        question_animation.set_opacity(0.0)
        self.play(question_animation, run_time=2.0)
        self.wait(1.0)

        # Animate answer
        answer_text = Text(
            "To make hot chocolate, combine cocoa powder,\n"
            "sugar, and salt in a saucepan, whisk in milk, heat\n"
            "until steaming, stir in vanilla extract, and serve.", font_size=12
        )
        answer_text.move_to(chat_gpt_text_box.get_center())
        answer_text.set_opacity(0.0)

        answer_animation = answer_text.animate
        answer_animation.move_to(chat_gpt_text_box.get_center() + [0.0, 2.0, 0.0])
        answer_animation.set_opacity(1.0)
        self.play(answer_animation, run_time=2.0)
        self.wait(3.0)