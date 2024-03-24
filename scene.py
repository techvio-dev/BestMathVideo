from manim import *
import numpy as np

class MyGraph(VGroup):
    def __init__(self, node_positions, edges, graph_shift=np.array([0, 0, 0]), scale_factor=0.5, **kwargs):
        super().__init__(**kwargs)
        self.node_positions = node_positions
        self.edges = edges
        self.graph_shift = graph_shift
        self.scale_factor = scale_factor
        self.create_vertices()
        self.create_edges()

    def create_vertices(self):
        for node, pos in self.node_positions.items():
            pos_with_shift = pos * self.scale_factor + self.graph_shift
            vertex = Dot(pos_with_shift, color=WHITE)
            self.add(vertex)

    def create_edges(self):
        for start_node, end_node in self.edges:
            start_pos = self.node_positions[start_node] * self.scale_factor + self.graph_shift
            end_pos = self.node_positions[end_node] * self.scale_factor + self.graph_shift
            edge_line = Line(start=start_pos, end=end_pos, stroke_width=DEFAULT_STROKE_WIDTH)
            self.add(edge_line)

class GraphTheory(Scene):
    def construct(self):
        node_positions = {
            "A": np.array([-5, -1, 0]), 
            "B": np.array([-4, 3, 0]), 
            "C": np.array([-1, 4, 0]), 
            "D": np.array([-2, 1, 0]),
            "E": np.array([1, 2, 0]),
            "F": np.array([1.5, 4.5, 0]), 
        }
        edges = [
            ("A", "B"),
            ("B", "C"),
            ("D", "C"),
            ("C", "E"),
            ("C", "F"),
            ("F", "E"),
            ("E", "D"),
            ("D", "B")
        ]
        graph_shift = np.array([-0.9, 0.9, 0])
        my_graph = MyGraph(node_positions, edges, graph_shift=graph_shift)

        self.play(Create(my_graph), run_time=5)
        self.wait(1)
        t1 = Text("Let's first define what a graph is", font="Lucida Console", font_size=30).shift(DOWN * 2)
        self.play(Write(t1))
        self.play(AnimationGroup(t1.animate.scale(0.75).next_to(my_graph, buff=0)))
        t2 = MarkupText(
            f"""
                A <span fgcolor="{RED}">graph</span> is a mathematical structure that visualizes
            """,
            font="Lucida Console",
            font_size=30
        ).move_to([0, 0, 0])
        t21 = MarkupText(
            f"""
                <span fgcolor="{BLUE}">connections</span> between various <span fgcolor="{GREEN}">components</span>.
            """,
            font="Lucida Console",
            font_size=30
        ).next_to(t2, DOWN, buff=0)
        t2_2 = MarkupText(
            f"""
                These components are called <span fgcolor="{GREEN}">nodes or vertices</span>
            """,
            font="Lucida Console",
            font_size=30
        ).next_to(t2, DOWN * 1.5, buff=0.6)
        t21_2 = MarkupText(
            f"""
                and the connections between them are called <span fgcolor="{BLUE}">edges</span>.
            """,
            font="Lucida Console",
            font_size=30
        ).next_to(t2_2, DOWN, buff=0)
        self.play(Write(t2), run_time=3)
        self.play(Write(t21), run_time=2)
        self.wait(1)
        self.play(Write(t2_2), run_time=3)
        self.play(Write(t21_2), run_time=3)
        self.wait(1)
        t3 = MarkupText(
            f"""
                <span fgcolor="{GREEN}">Graph Theory</span> allows us to analyze and model complex
            """,
            font="Lucida Console",
            font_size=30
        ).next_to(t21_2, DOWN, buff=0.5)
        t31 = MarkupText(
            f"""
                <span fgcolor="{BLUE}">interconnected systems</span> across different fields.
            """,
            font="Lucida Console",
            font_size=30
        ).next_to(t3, DOWN, buff=0)
        self.play(Write(t3), run_time=2.5)
        self.play(Write(t31), run_time=2.5)
        self.wait(1)
