from manim import *

class HelloWorld(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play( Write(text) )    # Write animation 으로 텍스트 출력
        self.wait()