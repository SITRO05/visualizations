from manim import *

class PythagoreanTheorem(Scene):
    def construct(self):
        # Title
        title = Text("Pythagorean Theorem: a² + b² = c²", font_size=36)
        title.to_edge(UP)
        self.play(Write(title))
        
        # Create right triangle
        triangle = Polygon(
            [-2, -1, 0],  # Point A
            [2, -1, 0],   # Point B
            [2, 2, 0],    # Point C
            color=WHITE
        )
        triangle.set_fill(BLUE, opacity=0.3)
        
        # Label sides
        a_label = MathTex("a").next_to(triangle.get_edge_center(DOWN), DOWN)
        b_label = MathTex("b").next_to(triangle.get_edge_center(RIGHT), RIGHT)
        c_label = MathTex("c").next_to(triangle.get_edge_center(UP+LEFT), UP+LEFT)
        
        # Show triangle
        self.play(Create(triangle))
        self.play(Write(a_label), Write(b_label), Write(c_label))
        self.wait(1)
        
        # Create squares on each side
        square_a = Square(side_length=3).next_to(triangle.get_edge_center(DOWN), DOWN)
        square_b = Square(side_length=3).next_to(triangle.get_edge_center(RIGHT), RIGHT)
        square_c = Square(side_length=3).rotate(45).next_to(triangle.get_edge_center(UP+LEFT), UP+LEFT)
        
        square_a.set_fill(RED, opacity=0.3)
        square_b.set_fill(GREEN, opacity=0.3)
        square_c.set_fill(YELLOW, opacity=0.3)
        
        # Transform triangle sides to squares
        self.play(
            ReplacementTransform(triangle.copy(), square_a),
            ReplacementTransform(triangle.copy(), square_b),
            ReplacementTransform(triangle.copy(), square_c)
        )
        self.wait(1)
        
        # Show area formulas
        area_a = MathTex("a^2").move_to(square_a.get_center())
        area_b = MathTex("b^2").move_to(square_b.get_center())
        area_c = MathTex("c^2").move_to(square_c.get_center())
        
        self.play(
            Write(area_a),
            Write(area_b),
            Write(area_c)
        )
        self.wait(2)
        
        # Final equation
        equation = MathTex("a^2 + b^2 = c^2").scale(1.5)
        equation.to_edge(DOWN)
        self.play(Write(equation))
        self.wait(2)

class FunctionPlot(Scene):
    def construct(self):
        # Axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-2, 2, 1],
            axis_config={"color": BLUE},
        )
        axes_labels = axes.get_axis_labels(x_label="x", y_label="f(x)")
        
        # Graph
        graph = axes.plot(lambda x: x**2, x_range=[-2, 2], color=YELLOW)
        graph_label = axes.get_graph_label(graph, label="x^2")
        
        # Show
        self.play(Create(axes), Write(axes_labels))
        self.play(Create(graph), Write(graph_label))
        self.wait(2)
        
        # Animate a point moving along the curve
        dot = Dot(color=RED).move_to(axes.coords_to_point(-2, 4))
        self.play(Create(dot))
        
        # Move dot along the graph
        self.play(
            MoveAlongPath(dot, graph, rate_func=linear),
            run_time=3
        )
        self.wait(1)