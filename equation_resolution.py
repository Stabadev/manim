from manim import *
from manim.utils.tex import TexTemplate

class EquationResolutionScene(Scene):
    def construct(self):
        # Définir la couleur de fond en blanc
        self.camera.background_color = WHITE

        # Définir la couleur du texte en noir
        text_color = BLACK

        # Spécifier la police sans-serif et en gras pour le texte
        font_kwargs = {
            "font": "DejaVu Sans",
            "weight": "BOLD",
        }

        # Créer un TexTemplate personnalisé pour les équations
        tex_template = TexTemplate()
        tex_template.add_to_preamble(r"\usepackage{sfmath}")
        tex_template.add_to_preamble(r"\renewcommand{\familydefault}{\sfdefault}")
        tex_template.add_to_preamble(r"\boldmath")  # Pour mettre les équations en gras

        # Ajouter la musique de fond
        self.add_sound("AcousticGuitar1.mp3")

        # Message d'introduction
        intro_text = Text(
            "Made with the Manim Python module",
            font_size=36,
            color=text_color,
            **font_kwargs
        )
        self.play(Write(intro_text))
        self.wait(2)
        self.play(FadeOut(intro_text))

        # Étape 1 : Écrire l'équation initiale
        eq1 = MathTex(
            "3x^2", "-", "108", "=", "0",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5)
        self.play(Write(eq1))
        self.wait(1)

        # Commentaire en anglais
        comment1 = Text(
            "We start with the initial equation.",
            font_size=24,
            color=text_color,
            **font_kwargs
        ).next_to(eq1, DOWN)
        self.play(Write(comment1))
        self.wait(2)
        self.play(FadeOut(comment1))

        # Étape 2 : Écrire -108 comme -3×36
        eq1_5 = MathTex(
            "3x^2", "-", "3 \\times 36", "=", "0",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5)
        self.play(TransformMatchingTex(eq1, eq1_5))
        self.wait(1)

        # Commentaire
        comment2 = Text(
            "Express -108 as -3×36.",
            font_size=24,
            color=text_color,
            **font_kwargs
        ).next_to(eq1_5, DOWN)
        self.play(Write(comment2))
        self.wait(2)
        self.play(FadeOut(comment2))

        # Étape 3 : Factoriser par 3
        eq2 = MathTex(
            "3", "(", "x^2", "-", "36", ")", "=", "0",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5)
        self.play(TransformMatchingTex(eq1_5, eq2))
        self.wait(1)

        # Commentaire
        comment3 = Text(
            "Factor out 3.",
            font_size=24,
            color=text_color,
            **font_kwargs
        ).next_to(eq2, DOWN)
        self.play(Write(comment3))
        self.wait(2)
        self.play(FadeOut(comment3))

        # Nouvelle Étape : Diviser les deux côtés par 3
        eq2_5 = MathTex(
            "\\frac{3(x^2 - 36)}{3}", "=", "\\frac{0}{3}",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5)
        self.play(TransformMatchingTex(eq2, eq2_5))
        self.wait(1)

        # Commentaire
        comment3_5 = Text(
            "Divide both sides by 3.",
            font_size=24,
            color=text_color,
            **font_kwargs
        ).next_to(eq2_5, DOWN)
        self.play(Write(comment3_5))
        self.wait(2)
        self.play(FadeOut(comment3_5))

        # Simplifier après division
        eq3 = MathTex(
            "x^2", "-", "36", "=", "0",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5)
        self.play(TransformMatchingTex(eq2_5, eq3))
        self.wait(1)

        # Commentaire
        comment4 = Text(
            "Simplify the equation.",
            font_size=24,
            color=text_color,
            **font_kwargs
        ).next_to(eq3, DOWN)
        self.play(Write(comment4))
        self.wait(2)
        self.play(FadeOut(comment4))

        # Étape 4 : Écrire 36 comme 6²
        eq4 = MathTex(
            "x^2", "-", "6^2", "=", "0",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(1)

        # Commentaire
        comment5 = Text(
            "Express 36 as 6 squared.",
            font_size=24,
            color=text_color,
            **font_kwargs
        ).next_to(eq4, DOWN)
        self.play(Write(comment5))
        self.wait(2)
        self.play(FadeOut(comment5))

        # Étape 5 : Appliquer l'identité remarquable
        eq5 = MathTex(
            "(", "x", "-", "6", ")", "(", "x", "+", "6", ")", "=", "0",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5)
        self.play(TransformMatchingTex(eq4, eq5))
        self.wait(1)

        # Commentaire
        comment6 = Text(
            "Apply the difference of squares formula.",
            font_size=24,
            color=text_color,
            **font_kwargs
        ).next_to(eq5, DOWN)
        self.play(Write(comment6))
        self.wait(2)
        self.play(FadeOut(comment6))

        # Étape 6 : Poser chaque facteur égal à zéro
        eq6_1 = MathTex(
            "x", "-", "6", "=", "0",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5).shift(UP*1.5)
        eq6_2 = MathTex(
            "x", "+", "6", "=", "0",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5).next_to(eq6_1, DOWN, buff=1)
        self.play(FadeOut(eq5))
        self.play(Write(eq6_1), Write(eq6_2))
        self.wait(1)

        # Commentaire
        comment7 = Text(
            "Set each factor equal to zero.",
            font_size=24,
            color=text_color,
            **font_kwargs
        ).next_to(eq6_2, DOWN)
        self.play(Write(comment7))
        self.wait(2)
        self.play(FadeOut(comment7))

        # Résoudre x - 6 = 0
        eq7_1 = MathTex(
            "x", "-", "6", "+", "6", "=", "0", "+", "6",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5).shift(UP*1.5)
        self.play(Transform(eq6_1, eq7_1))
        self.wait(1)

        # Simplifier pour obtenir x = 6
        sol1 = MathTex(
            "x", "=", "6",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5).move_to(eq6_1)
        self.play(Transform(eq6_1, sol1))
        self.wait(1)

        # Résoudre x + 6 = 0
        eq7_2 = MathTex(
            "x", "+", "6", "-", "6", "=", "0", "-", "6",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5).move_to(eq6_2)
        self.play(Transform(eq6_2, eq7_2))
        self.wait(1)

        # Simplifier pour obtenir x = -6
        sol2 = MathTex(
            "x", "=", "-6",
            color=text_color,
            tex_template=tex_template
        ).scale(1.5).move_to(eq6_2)
        self.play(Transform(eq6_2, sol2))
        self.wait(1)

        # Commentaire
        comment8 = Text(
            "Solve each equation by isolating x.",
            font_size=24,
            color=text_color,
            **font_kwargs
        ).next_to(sol2, DOWN)
        self.play(Write(comment8))
        self.wait(2)
        self.play(FadeOut(comment8))

        # Étape 9 : Conclusion
        conclusion = Text(
            "The solutions are x = -6 and x = 6.",
            font_size=36,
            color=text_color,
            **font_kwargs
        ).shift(DOWN)
        self.play(FadeOut(sol1, sol2))
        self.play(Write(conclusion))
        self.wait(3)

        # Effacer le texte de conclusion avant d'afficher le message de fin
        self.play(FadeOut(conclusion))

        # Message de fin au même endroit que le texte précédent
        end_text = Text(
            "Python code available on github.com/Stabadev/manim",
            font_size=30,
            color=text_color,
            **font_kwargs
        ).shift(DOWN)  # Position identique à 'conclusion'
        self.play(Write(end_text))
        self.wait(3)


