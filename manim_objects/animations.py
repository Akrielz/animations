from manim import Mobject


def fade_in_animation(mobject: Mobject):
    mobject.set_opacity(0.0)
    mobject_animated = mobject.animate
    mobject_animated.set_opacity(1.0)
    return mobject_animated
