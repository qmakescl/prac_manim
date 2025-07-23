from manim import *

class FunctionPlot(Scene):
    def construct(self):
        ax = Axes(
            x_range=[-5, 5, 1],
            y_range=[-3, 3, 1],
            x_length=8,
            y_length=4,
            axis_config={"include_numbers": True},
        )
        func = lambda x: 0.1 * (x**2)
        curve = ax.plot(func, color=YELLOW)
        self.play(Create(ax))
        self.play(Write(curve))
        self.wait()