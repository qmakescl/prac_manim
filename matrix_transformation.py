from manim import *
import numpy as np # numpy import 추가

class MatrixTransformations(Scene):
    def construct(self):
        # 씬 제목
        title = Text("행렬 변환 (Matrix Transformation)").to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        # 1. 초기 그리드 및 벡터 설정
        # 좌표계 생성
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=10,
            y_length=10,
            axis_config={"color": GREY_A},
            background_line_style={"stroke_color": GREY_B, "stroke_width": 1, "stroke_opacity": 0.6}
        )
        # 단위 벡터 (기저 벡터)
        i_hat = Arrow(ORIGIN, RIGHT, buff=0).set_color(RED).set_length(1)
        j_hat = Arrow(ORIGIN, UP, buff=0).set_color(GREEN).set_length(1)
        
        # 벡터 레이블
        i_label = MathTex("\\mathbf{e}_1 = \\begin{pmatrix} 1 \\\\ 0 \end{pmatrix}").next_to(i_hat, RIGHT, buff=0.1).set_color(RED)
        j_label = MathTex("\\mathbf{e}_2 = \\begin{pmatrix} 0 \\\\ 1 \end{pmatrix}").next_to(j_hat, UP, buff=0.1).set_color(GREEN)

        self.play(Create(grid), Create(i_hat), Create(j_hat), Write(i_label), Write(j_label))
        self.wait(1)

        # 2. 크기 조절 (Scaling) 변환
        self.play(FadeOut(i_label, j_label)) # 이전 레이블 제거
        self.next_section("Scaling")
        
        scaling_matrix = np.array([[2, 0], [0, 0.5]]) # 행렬 변수화
        scaling_matrix_tex = MathTex(
            "A_{scale} = \\begin{pmatrix} 2 & 0 \\\\ 0 & 0.5 \end{pmatrix}",
            font_size=50
        ).to_edge(UP).shift(DOWN*0.5)

        self.play(Transform(title, Text("1. 크기 조절 (Scaling)").to_edge(UP)), Write(scaling_matrix_tex))
        self.wait(1)

        # 그리드 및 벡터에 변환 적용
        self.play(
            grid.animate.apply_matrix(scaling_matrix),
            i_hat.animate.apply_matrix(scaling_matrix),
            j_hat.animate.apply_matrix(scaling_matrix),
            run_time=2
        )
        self.wait(1)

        # 3. 회전 (Rotation) 변환
        self.play(
            FadeOut(scaling_matrix_tex),
            grid.animate.apply_matrix(np.linalg.inv(scaling_matrix)), # 그리드 원상 복구 (역행렬 적용)
            i_hat.animate.set_color(RED).set_length(1).move_to(ORIGIN).shift(RIGHT), # 벡터 원상 복구
            j_hat.animate.set_color(GREEN).set_length(1).move_to(ORIGIN).shift(UP), # 벡터 원상 복구
            run_time=2
        )
        self.next_section("Rotation")

        theta = PI / 4 # 45도
        rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]]) # 행렬 변수화
        rotation_matrix_tex = MathTex(
            "A_{rotate} = \\begin{pmatrix} \\cos\\theta & -\\sin\\theta \\\\ \\sin\\theta & \\cos\\theta \end{pmatrix}",
            font_size=50
        ).to_edge(UP).shift(DOWN*0.5)
        
        self.play(Transform(title, Text("2. 회전 (Rotation)").to_edge(UP)), Write(rotation_matrix_tex))
        self.wait(1)

        self.play(
            grid.animate.apply_matrix(rotation_matrix),
            i_hat.animate.apply_matrix(rotation_matrix),
            j_hat.animate.apply_matrix(rotation_matrix),
            run_time=2
        )
        self.wait(1)

        # 4. 전단 (Shear) 변환
        self.play(
            FadeOut(rotation_matrix_tex),
            grid.animate.apply_matrix(np.linalg.inv(rotation_matrix)), # 그리드 원상 복구 (역행렬 적용)
            i_hat.animate.set_color(RED).set_length(1).move_to(ORIGIN).shift(RIGHT), # 벡터 원상 복구
            j_hat.animate.set_color(GREEN).set_length(1).move_to(ORIGIN).shift(UP), # 벡터 원상 복구
            run_time=2
        )
        self.next_section("Shear")

        shear_matrix = np.array([[1, 1.5], [0, 1]]) # 행렬 변수화
        shear_matrix_tex = MathTex(
            "A_{shear} = \\begin{pmatrix} 1 & 1.5 \\\\ 0 & 1 \end{pmatrix}",
            font_size=50
        ).to_edge(UP).shift(DOWN*0.5)

        self.play(Transform(title, Text("3. 전단 (Shear)").to_edge(UP)), Write(shear_matrix_tex))
        self.wait(1)

        self.play(
            grid.animate.apply_matrix(shear_matrix),
            i_hat.animate.apply_matrix(shear_matrix),
            j_hat.animate.apply_matrix(shear_matrix),
            run_time=2
        )
        self.wait(1)

        # 5. 반사 (Reflection) 변환
        self.play(
            FadeOut(shear_matrix_tex),
            grid.animate.apply_matrix(np.linalg.inv(shear_matrix)), # 그리드 원상 복구 (역행렬 적용)
            i_hat.animate.set_color(RED).set_length(1).move_to(ORIGIN).shift(RIGHT), # 벡터 원상 복구
            j_hat.animate.set_color(GREEN).set_length(1).move_to(ORIGIN).shift(UP), # 벡터 원상 복구
            run_time=2
        )
        self.next_section("Reflection")

        reflection_matrix = np.array([[-1, 0], [0, 1]]) # 행렬 변수화
        reflection_matrix_tex = MathTex(
            "A_{reflect} = \\begin{pmatrix} -1 & 0 \\\\ 0 & 1 \end{pmatrix}",
            font_size=50
        ).to_edge(UP).shift(DOWN*0.5)

        self.play(Transform(title, Text("4. 반사 (Reflection)").to_edge(UP)), Write(reflection_matrix_tex))
        self.wait(1)

        self.play(
            grid.animate.apply_matrix(reflection_matrix),
            i_hat.animate.apply_matrix(reflection_matrix),
            j_hat.animate.apply_matrix(reflection_matrix),
            run_time=2
        )
        self.wait(1)

        # 6. 평행 이동 (Translation) - 동차 좌표계 설명
        self.play(
            FadeOut(reflection_matrix_tex),
            grid.animate.apply_matrix(np.linalg.inv(reflection_matrix)), # 그리드 원상 복구 (역행렬 적용)
            i_hat.animate.set_color(RED).set_length(1).move_to(ORIGIN).shift(RIGHT), # 벡터 원상 복구
            j_hat.animate.set_color(GREEN).set_length(1).move_to(ORIGIN).shift(UP), # 벡터 원상 복구
            run_time=2
        )
        self.next_section("Translation")

        translation_title = Text("5. 평행 이동 (Translation)").to_edge(UP)
        homogeneous_coords_text = Text(
            "평행 이동은 동차 좌표계를 사용하여 행렬 곱셈으로 표현합니다.",
            font_size=30
        ).next_to(translation_title, DOWN, buff=0.5)

        self.play(Transform(title, translation_title), Write(homogeneous_coords_text))
        self.wait(1)

        # 임의의 점 생성
        point = Dot(point=np.array([1, 1, 0]), color=BLUE)
        point_label = MathTex("P(1,1)").next_to(point, UL, buff=0.1)
        self.play(Create(point), Write(point_label))
        self.wait(1)

        tx, ty = 2, 3
        translation_matrix_tex = MathTex(
            "T = \\begin{pmatrix} 1 & 0 & t_x \\\\ 0 & 1 & t_y \\\\ 0 & 0 & 1 \end{pmatrix} = \\begin{pmatrix} 1 & 0 & 2 \\\\ 0 & 1 & 3 \\\\ 0 & 0 & 1 \end{pmatrix}",
            font_size=40
        ).next_to(homogeneous_coords_text, DOWN, buff=0.5)

        self.play(Write(translation_matrix_tex))
        self.wait(1)

        # 점 이동 애니메이션 (Manim의 shift() 사용)
        self.play(point.animate.shift(RIGHT*tx + UP*ty), run_time=2)
        transformed_point_label = MathTex(f"P'({1+tx},{1+ty})").next_to(point, UR, buff=0.1)
        self.play(Transform(point_label, transformed_point_label))
        self.wait(2)

        # 최종 정리
        self.play(
            FadeOut(grid, i_hat, j_hat, point, point_label, title, homogeneous_coords_text, translation_matrix_tex)
        )
        self.wait(3)
