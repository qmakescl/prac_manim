from manim import *

class TransformerArchitecture(Scene):
    def construct(self):
        # 인코더 블록 생성
        encoder_block = Rectangle(width=3, height=2, color=BLUE, fill_opacity=0.6).set_stroke(width=3)
        encoder_text = Text("인코더", font_size=36).move_to(encoder_block.get_center())
        encoder_group = VGroup(encoder_block, encoder_text)

        # 디코더 블록 생성
        decoder_block = Rectangle(width=3, height=2, color=GREEN, fill_opacity=0.6).set_stroke(width=3)
        decoder_text = Text("디코더", font_size=36).move_to(decoder_block.get_center())
        decoder_group = VGroup(decoder_block, decoder_text)

        # 위치 조정
        encoder_group.shift(LEFT * 3)
        decoder_group.shift(RIGHT * 3)

        # 블록 생성 애니메이션
        self.play(Create(encoder_group), Create(decoder_group))
        self.wait(0.5)

        # 스택 표현 (개념적)
        encoder_stack_label = Text("N개의 인코더 레이어", font_size=24).next_to(encoder_group, UP, buff=0.5)
        decoder_stack_label = Text("N개의 디코더 레이어", font_size=24).next_to(decoder_group, UP, buff=0.5)
        self.play(Write(encoder_stack_label), Write(decoder_stack_label))
        self.wait(0.5)

        # 데이터 흐름 화살표
        flow_arrow = Arrow(encoder_group.get_right(), decoder_group.get_left(), buff=0.2, color=PURPLE, stroke_width=5)
        flow_text = Text("컨텍스트 벡터", font_size=28).next_to(flow_arrow, UP)
        self.play(Create(flow_arrow), Write(flow_text))
        self.wait(1)