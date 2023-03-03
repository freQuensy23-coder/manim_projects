from manim import *


def dipole(x, y, r, d, c1=RED, c2=BLUE, fill=True):
    c1, c2 = Circle(color=c1, radius=r), Circle(color=c2, radius=r)
    c1.shift(LEFT * d / 2)
    c2.shift(RIGHT * d / 2)
    if fill:
        c1.set_fill(opacity=0.6)
        c2.set_fill(opacity=0.6)
    l = Line((d / 2, 0, 0), (-d / 2, 0, 0))
    res = VGroup(l, c1, c2)
    res.shift(UP * y + RIGHT * x)
    return res


class CreateCircle(Scene):
    def construct(self):
        square = Square(color=RED)
        square.set_fill(opacity=0.6)
        self.play(Create(square, run_time=2))
        lambda_text = Tex(r"$\lambda$")
        self.add(lambda_text)
        dip_params = x, y, r, d = 2, 2, 0.1, 0.55
        dip = dipole(*dip_params)
        self.play(ShowIncreasingSubsets(dip))
        self.wait(2)

        square_with_text = VGroup(square, lambda_text)
        self.play(square_with_text.animate.shift(LEFT*d))
        self.play(square_with_text.animate.shift(RIGHT * d))
        self.play(square_with_text.animate.shift(LEFT * d))
        self.play(square_with_text.animate.shift(RIGHT * d))

        blue_square = Rectangle(color=BLUE, height=square.height, width=square.width - d)
        blue_square.set_fill(opacity=0.6)
        minus_lambda_text = Tex(r"$ - \lambda$", color=BLUE)
        self.add(minus_lambda_text)
        self.play(FadeIn(blue_square))
        self.wait(4)


