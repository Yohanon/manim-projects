from svgelements import Curve, Move

from manim import *


class MiniCurve(Scene):
    def construct(self) :
        curve = ParametricFunction(lambda t: [3*np.sin(3*t), 3*np.sin(4*t),0], t_range=[0 ,TAU])
        curve.set_color_by_gradient(PURPLE, BLUE, TEAL).set_stroke(width=8)
        dot = Dot(curve.get_start(), color=WHITE)
        self.play(Create(curve), MoveAlongPath(dot, curve), run_time=4, rate_func=linear)
        self.play(FadeOut(dot), curve.animate.scale(0.8).rotate(PI / 4), run_time=1.5)
        self.wait()
