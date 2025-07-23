from manim import *
import numpy as np

class EigenDecomposition(Scene):
    def construct(self):
        # 0. 제목 및 소개
        # Tex 대신 Text를 사용하여 한글을 렌더링합니다. 
        # 시스템에 따라 "NanumGothic" 또는 "Malgun Gothic" 등 사용 가능한 한글 폰트로 변경하세요.
        title = Text("행렬의 고유값과 고유벡터", font="NanumGothic", weight=BOLD).to_edge(UP)
        self.play(Write(title))
        self.wait(1)

        intro_text = Text("행렬의 선형 변환이 벡터에 미치는 영향을 시각화합니다.", font="NanumGothic").next_to(title, DOWN)
        self.play(Write(intro_text))
        self.wait(1)
        self.play(FadeOut(intro_text))

        # 1. 행렬 및 벡터 정의
        matrix_A_text = MathTex("A = ", r"\begin{pmatrix} 4 & 2 \\ 1 & 3 \end{pmatrix}").to_corner(UL).shift(RIGHT*1.5)
        self.play(Write(matrix_A_text))
        self.wait(0.5)

        # 2. 좌표계 설정 및 임의의 벡터 변환 시각화
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={"stroke_opacity": 0.3},
            x_length=7,
            y_length=7
        ).to_edge(RIGHT)
        # get_axis_labels()를 사용하여 x, y 축 레이블을 한 번에 가져옵니다.
        grid_labels = grid.get_axis_labels()
        self.play(Create(grid), Create(grid_labels))
        self.wait(0.5)

        # 임의의 벡터
        initial_vector_coords = np.array([1, 1])
        initial_vector = Vector(initial_vector_coords).set_color(BLUE)
        initial_vector_label = MathTex(r"\mathbf{x}").next_to(initial_vector, UR)

        # 변환된 벡터 (A @ x)
        A_val = np.array([[4, 2], [1, 3]])
        transformed_vector_coords = A_val @ initial_vector_coords
        transformed_vector = Vector(transformed_vector_coords).set_color(RED)
        transformed_vector_label = MathTex(r"A\mathbf{x}").next_to(transformed_vector, UR)

        self.play(Create(initial_vector), Write(initial_vector_label))
        self.wait(1)
        self.play(
            ReplacementTransform(initial_vector, transformed_vector),
            ReplacementTransform(initial_vector_label, transformed_vector_label)
        )
        self.wait(1.5)

        # 설명
        # 한글과 수식을 분리하여 VGroup으로 묶음
        transform_explanation = VGroup(
            Text("대부분의 벡터는 행렬 ", font="NanumGothic"),
            MathTex("A"),
            Text("에 의해 방향과 크기가 모두 변합니다.", font="NanumGothic")
        ).arrange(RIGHT, buff=0.1).next_to(matrix_A_text, DOWN, buff=0.5)
        self.play(Write(transform_explanation))
        self.wait(2)
        self.play(
            FadeOut(transformed_vector), FadeOut(transformed_vector_label),
            FadeOut(transform_explanation)
        )
        self.wait(0.5)

        # 3. 고유벡터 개념 도입
        eigen_intro_text = Text("하지만, 특별한 벡터는 방향이 변하지 않습니다.", font="NanumGothic").next_to(matrix_A_text, DOWN, buff=0.5)
        self.play(Write(eigen_intro_text))
        self.wait(1.5)

        # 고유값 및 고유벡터 계산 (NumPy 사용)
        eigenvalues, eigenvectors = np.linalg.eig(A_val)
        
        # 첫 번째 고유벡터 시각화
        eigenvector1_coords = eigenvectors[:, 0]
        eigenvector1 = Vector(eigenvector1_coords).set_color(GREEN)
        eigenvector1_label = MathTex(r"\mathbf{v}_1").next_to(eigenvector1, UL)

        # 변환된 첫 번째 고유벡터
        transformed_eigenvector1_coords = A_val @ eigenvector1_coords
        transformed_eigenvector1 = Vector(transformed_eigenvector1_coords).set_color(GREEN)
        transformed_eigenvector1_label = MathTex(r"A\mathbf{v}_1 = \lambda_1 \mathbf{v}_1").next_to(transformed_eigenvector1, UL)


        self.play(Create(eigenvector1), Write(eigenvector1_label))
        self.wait(1)
        self.play(
            ReplacementTransform(eigenvector1, transformed_eigenvector1),
            ReplacementTransform(eigenvector1_label, transformed_eigenvector1_label)
        )
        self.wait(2)

        # 두 번째 고유벡터 시각화
        eigenvector2_coords = eigenvectors[:, 1]
        eigenvector2 = Vector(eigenvector2_coords).set_color(PURPLE)
        eigenvector2_label = MathTex(r"\mathbf{v}_2").next_to(eigenvector2, UR)

        # 변환된 두 번째 고유벡터
        transformed_eigenvector2_coords = A_val @ eigenvector2_coords
        transformed_eigenvector2 = Vector(transformed_eigenvector2_coords).set_color(PURPLE)
        transformed_eigenvector2_label = MathTex(r"A\mathbf{v}_2 = \lambda_2 \mathbf{v}_2").next_to(transformed_eigenvector2, UR)

        self.play(
            FadeOut(transformed_eigenvector1), FadeOut(transformed_eigenvector1_label),
            FadeOut(eigen_intro_text)
        )
        self.wait(0.5)
        self.play(Create(eigenvector2), Write(eigenvector2_label))
        self.wait(1)
        self.play(
            ReplacementTransform(eigenvector2, transformed_eigenvector2),
            ReplacementTransform(eigenvector2_label, transformed_eigenvector2_label)
        )
        self.wait(2)

        self.play(
            FadeOut(transformed_eigenvector2), FadeOut(transformed_eigenvector2_label)
        )

        # 4. 고유값 방정식 설명
        eigen_eq = MathTex(r"A\mathbf{v} = \lambda\mathbf{v}").move_to(matrix_A_text.get_center() + DOWN * 2)
        
        # 한글과 수식을 분리하여 VGroup으로 묶음
        eigen_eq_explanation = VGroup(
            Text("이때 ", font="NanumGothic"),
            MathTex(r"\mathbf{v}"),
            Text("를 고유벡터, ", font="NanumGothic"),
            MathTex(r"\lambda"),
            Text("를 고유값이라고 합니다.", font="NanumGothic")
        ).arrange(RIGHT, buff=0.1).next_to(eigen_eq, DOWN)
        self.play(Write(eigen_eq))
        self.play(Write(eigen_eq_explanation))
        self.wait(2)
        self.play(FadeOut(eigen_eq_explanation))

        # 5. 특성 방정식 유도
        char_eq_step1 = MathTex(r"A\mathbf{v} - \lambda\mathbf{v} = \mathbf{0}").move_to(eigen_eq.get_center())
        char_eq_step2 = MathTex(r"A\mathbf{v} - \lambda I\mathbf{v} = \mathbf{0}").move_to(eigen_eq.get_center())
        char_eq_step3 = MathTex(r"(A - \lambda I)\mathbf{v} = \mathbf{0}").move_to(eigen_eq.get_center())
        char_eq_step4 = MathTex(r"\det(A - \lambda I) = 0").move_to(eigen_eq.get_center()).set_color(YELLOW)
        char_eq_name = Text("특성 방정식", font="NanumGothic").next_to(char_eq_step4, DOWN)

        self.play(TransformMatchingTex(eigen_eq, char_eq_step1))
        self.wait(1)
        self.play(TransformMatchingTex(char_eq_step1, char_eq_step2))
        self.wait(1)
        self.play(TransformMatchingTex(char_eq_step2, char_eq_step3))
        self.wait(1)
        self.play(TransformMatchingTex(char_eq_step3, char_eq_step4))
        self.play(Write(char_eq_name))
        self.wait(2)

        self.play(
            FadeOut(char_eq_step4), FadeOut(char_eq_name),
            FadeOut(matrix_A_text)
        )

        # 6. 고유값 및 고유벡터 결과 표시
        eigen_result_text = Text("계산된 고유값과 고유벡터", font="NanumGothic").to_corner(UL)
        self.play(Write(eigen_result_text))

        # NumPy로 계산된 실제 값
        lambda1_val = eigenvalues[0]
        v1_val = eigenvectors[:, 0]
        lambda2_val = eigenvalues[1]
        v2_val = eigenvectors[:, 1]

        result_lambda1 = MathTex(rf"\lambda_1 = {lambda1_val:.2f}").next_to(eigen_result_text, DOWN, buff=0.5)
        result_v1 = MathTex(rf"\mathbf{v1_val}_1 = \begin{{pmatrix}} {v1_val[0]:.2f} \\ {v1_val[1]:.2f} \end{{pmatrix}}").next_to(result_lambda1, RIGHT, buff=1)

        result_lambda2 = MathTex(rf"\lambda_2 = {lambda2_val:.2f}").next_to(result_lambda1, DOWN, buff=0.5)
        result_v2 = MathTex(rf"\mathbf{v2_val}_2 = \begin{{pmatrix}} {v2_val[0]:.2f} \\ {v2_val[1]:.2f} \end{{pmatrix}}").next_to(result_lambda2, RIGHT, buff=1)

        self.play(Write(result_lambda1), Write(result_v1))
        self.play(Write(result_lambda2), Write(result_v2))
        self.wait(2)

        # 최종 요약
        summary_text = Text("고유벡터는 변환 후에도 방향이 유지되는 특별한 벡터입니다.", font="NanumGothic").to_edge(DOWN)
        summary_text2 = Text("고유값은 그 고유벡터가 변환되는 크기 비율입니다.", font="NanumGothic").next_to(summary_text, DOWN)
        self.play(Write(summary_text))
        self.play(Write(summary_text2)) # summary_text2가 화면 밖으로 나갈 수 있어 분리
        self.wait(3)
        self.play(FadeOut(*self.mobjects))