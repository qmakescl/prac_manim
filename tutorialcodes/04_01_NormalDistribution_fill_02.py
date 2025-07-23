from manim import *
import numpy as np  # numpy import 추가
from scipy.stats import norm

class NormalDistribution(Scene):
    def construct(self):
        # 씬 제목
        title = Text("정규분포의 확률도표").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 정규분포 파라미터
        mu = 3
        sigma = 1

        # 1. 축(Axes) 객체를 먼저 생성합니다.
        # x_length와 y_length를 지정하여 화면에 맞는 크기로 조절합니다.
        axes = Axes(
            x_range=[mu - 4*sigma, mu + 4*sigma, 1],
            y_range=[0, 0.5, 0.1],
            x_length=8,
            y_length=4,
            axis_config={"color": BLUE},
            x_axis_config={
                "include_tip": False,  # x축의 화살표 끝 제거
            },
            # y축에만 적용될 설정을 지정하여 모든 시각적 요소를 제거합니다.
            y_axis_config={
                "stroke_opacity": 0,  # 축 선을 완전히 투명하게 만듭니다.
                "include_ticks": False, # 눈금을 그리지 않습니다.
                "include_tip": False,   # 화살표 끝을 그리지 않습니다.
            },
        )

        # 2. 애니메이션을 위해 두 종류의 그래프를 준비합니다.
        # (1) 곡선만 있는 그래프
        graph_curve = axes.plot(
            lambda x: norm.pdf(x, mu, sigma),
            color=YELLOW
        )

        # (2) 곡선 아래가 채워진 그래프
        graph_filled = axes.plot(
            lambda x: norm.pdf(x, mu, sigma),
            color=YELLOW,
            fill_color=RED,
            fill_opacity=0.5
        )

        # 3. 축과 곡선을 먼저 그리고, 그 다음에 채우기 애니메이션을 실행합니다.
        self.play(Create(axes), Create(graph_curve))
        self.wait(1)
        self.play(Transform(graph_curve, graph_filled)) # 곡선 그래프를 채워진 그래프로 변환
        self.wait(2)