from manim import *

class BasicShapes(Scene):
    def construct(self):
        # Create shapes
        circle = Circle()
        square = Square()
        triangle = Triangle()
        
        # Position them
        circle.shift(LEFT * 2)
        square.shift(RIGHT * 2)
        triangle.shift(DOWN * 2)
        
        # Set colors
        circle.set_fill(BLUE, opacity=0.5)
        square.set_fill(GREEN, opacity=0.5)
        triangle.set_fill(RED, opacity=0.5)
        
        # Animate
        self.play(Create(circle), Create(square), Create(triangle))
        self.wait(1)
        self.play(
            circle.animate.shift(RIGHT * 4),
            square.animate.shift(LEFT * 4),
            triangle.animate.shift(UP * 4)
        )
        self.wait(1)