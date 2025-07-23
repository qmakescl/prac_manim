from manim import *

class CreateCircle(Scene):
    def construct(self):
        circle = Circle()   # Circle 객체 생성
        circle.set_fill(BLUE, opacity=0.5)  # 파란색으로 채우기, 불투명도 0.5
        self.play( Create(circle) )   # Circle 생성 애니메이션 실행
        self.wait(1)