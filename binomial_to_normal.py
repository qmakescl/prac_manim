
from manim import *
import scipy.stats as stats
import numpy as np

class BinomialToNormal(Scene):
    def construct(self):
        # 초기 파라미터 설정
        n_values = [10, 30, 50, 100]
        p = 0.5
        axes = Axes(
            x_range=[0, 100, 10],
            y_range=[0, 0.15, 0.05],
            axis_config={"color": BLUE},
        )
        self.play(Create(axes))

        # n 값에 따라 이항분포와 정규분포를 업데이트하는 함수
        def get_binomial_dist(n, p, axes_obj):
            x_coords = np.arange(0, n + 1)
            y_coords = stats.binom.pmf(x_coords, n, p)
            bar_width = 0.8  # 막대의 너비 (좌표축 단위)

            # 막대들을 VGroup으로 묶어서 관리합니다.
            bars = VGroup()
            for x, y in zip(x_coords, y_coords):
                # 좌표축의 (x, 0)과 (x, y) 위치를 화면상의 점으로 변환합니다.
                bottom_point = axes_obj.c2p(x, 0)
                top_point = axes_obj.c2p(x, y)
                
                # 막대를 나타내는 사각형을 생성합니다.
                bar = Rectangle(
                    width=axes_obj.x_axis.get_unit_size() * bar_width,
                    height=top_point[1] - bottom_point[1], # 높이는 화면 y좌표의 차이입니다.
                    stroke_width=0,
                    fill_color=YELLOW,
                    fill_opacity=0.7
                )
                # 막대의 아래쪽 가장자리를 x축에 맞춥니다.
                bar.move_to(bottom_point, aligned_edge=DOWN)
                bars.add(bar)
            return bars

        def get_normal_dist(n, p):
            mu = n * p
            sigma = np.sqrt(n * p * (1 - p))
            # get_graph 대신 최신 Manim의 표준 메서드인 plot을 사용합니다.
            return axes.plot(lambda x: stats.norm.pdf(x, mu, sigma), x_range=[0, n])

        # 초기 분포 생성
        current_binomial_dist = get_binomial_dist(n_values[0], p, axes)
        current_normal_dist = get_normal_dist(n_values[0], p)
        n_label = MathTex(f"n = {n_values[0]}").to_corner(UL)

        self.play(Create(current_binomial_dist), Write(n_label))
        self.wait(1)
        self.play(Create(current_normal_dist))
        self.wait(1)

        # n 값을 변경하며 애니메이션 생성
        for i in range(1, len(n_values)):
            n = n_values[i]
            # n이 변하면 막대의 개수가 변하므로 Transform을 사용할 수 없습니다.
            # FadeOut/FadeIn으로 대체합니다.
            new_binomial_dist = get_binomial_dist(n, p, axes)
            new_normal_dist = get_normal_dist(n, p)
            new_n_label = MathTex(f"n = {n}").to_corner(UL)

            self.play(
                FadeOut(current_binomial_dist),
                FadeIn(new_binomial_dist),
                Transform(current_normal_dist, new_normal_dist),
                Transform(n_label, new_n_label),
                run_time=2
            )
            current_binomial_dist = new_binomial_dist # 다음 루프를 위해 참조를 업데이트합니다.
            self.wait(1)

        title = Text("이항분포에서 n 이 증가할수록 정규분포를 닮아갑니다.").scale(0.7).to_corner(UR)
        self.play(Write(title))
        self.wait(2)
