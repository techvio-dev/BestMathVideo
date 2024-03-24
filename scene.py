from manim import *
import numpy as np

class MyGraph(VGroup):
    def __init__(self, node_positions, edges, labels, graph_shift=np.array([0, 0, 0]), scale_factor=0.5, **kwargs):
        super().__init__(**kwargs)
        self.node_positions = node_positions
        self.edges = edges
        self.labels = labels
        self.graph_shift = graph_shift
        self.scale_factor = scale_factor
        self.vertices = VGroup()
        self.edge_lines = VGroup()
        self.create_edges()
        self.create_vertices()
        self.vertices.z_index = 2
        self.edge_lines.z_index = 1
        self.add(self.edge_lines, self.vertices)

    def create_vertices(self):
        dark_blue = "#236B8E"
        for node, pos in self.node_positions.items():
            pos_with_shift = pos * self.scale_factor + self.graph_shift
            vertex_circle = Circle(radius=0.2, color=WHITE, fill_color=dark_blue, fill_opacity=1, stroke_color=WHITE, stroke_width=2).move_to(pos_with_shift)
            self.vertices.add(vertex_circle)
            if node in self.labels:
                vertex_label = Text(self.labels[node], font_size=24, color=WHITE).move_to(pos_with_shift)
                self.vertices.add(vertex_label)

    def create_edges(self):
        for start_node, end_node in self.edges:
            start_pos = self.node_positions[start_node] * self.scale_factor + self.graph_shift
            end_pos = self.node_positions[end_node] * self.scale_factor + self.graph_shift
            edge_line = Line(start=start_pos, end=end_pos, stroke_width=DEFAULT_STROKE_WIDTH, color=GREY)
            self.edge_lines.add(edge_line)

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
        labels = {
            "A": "1", 
            "B": "2", 
            "C": "3", 
            "D": "4",
            "E": "5",
            "F": "6",
        }
        shift = np.array([-0.9, 1.3, 0])
        my_graph = MyGraph(node_positions, edges, labels, graph_shift=shift)
        
        self.play(Create(my_graph.vertices), run_time=2)
        self.play(Create(my_graph.edge_lines), run_time=2)
        self.wait(1)

        t1 = Text("Let's first define what a graph is", font="Lucida Console", font_size=30).shift(DOWN * 2)
        self.play(Write(t1))
        self.play(AnimationGroup(t1.animate.scale(0.75).next_to(my_graph, buff=0)))
        t2 = MarkupText(
            f"""
                A <span fgcolor="{RED}">graph</span> is a mathematical structure that visualizes
            """,a
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