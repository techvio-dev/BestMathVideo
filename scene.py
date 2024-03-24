from manim import *
import numpy as np

class MyGraph(VGroup):
	def __init__(self, node_positions, edges, labels, directed=False, graph_shift=np.array([0, 0, 0]), scale_factor=0.5, vertex_radius=0.2, **kwargs):
		super().__init__(**kwargs)
		self.node_positions = node_positions
		self.edges = edges
		self.labels = labels
		self.directed = directed
		self.graph_shift = graph_shift
		self.scale_factor = scale_factor
		self.vertex_radius = vertex_radius
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
			vertex_circle = Circle(radius=self.vertex_radius, color=WHITE, fill_color=dark_blue, fill_opacity=1, stroke_color=WHITE, stroke_width=4).move_to(pos_with_shift)
			self.vertices.add(vertex_circle)
			if node in self.labels:
				vertex_label = Text(self.labels[node], font_size=24, color=WHITE).move_to(pos_with_shift)
				self.vertices.add(vertex_label)

	def create_edges(self):
		for start_node, end_node in self.edges:
			start_pos = self.node_positions[start_node] * self.scale_factor + self.graph_shift
			end_pos = self.node_positions[end_node] * self.scale_factor + self.graph_shift
			if self.directed:
				edge_line = Arrow(start=start_pos, end=end_pos, buff=0.1, stroke_width=DEFAULT_STROKE_WIDTH, color=GREY, max_tip_length_to_length_ratio=0.05)  # Adjust arrowhead size if needed
			else:
				edge_line = Line(start=start_pos, end=end_pos, stroke_width=DEFAULT_STROKE_WIDTH, color=GREY)
			self.edge_lines.add(edge_line)

class GraphTheory(Scene):
	def construct(self):
		"""
		axes = Axes(
			x_range=[-10, 10, 1],
			y_range=[-6, 6, 1],
			x_length=config.frame_width - 1,
			y_length=config.frame_height - 1,
			axis_config={"color": BLUE},
		)

		self.add(axes)
		"""
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

		t1 = Text("Let's define what a graph is", font="Lucida Console", font_size=30).shift(DOWN * 2)
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

		self.play(FadeOut(t1), FadeOut(t2), FadeOut(t21), FadeOut(t2_2), FadeOut(t21_2), run_time=0.5)
		self.play(my_graph.animate.move_to(ORIGIN).scale(1.5), run_time=1)
		
		
		arrow_to_vertex = Arrow(np.array([-4, 2, 0]), np.array([-2, 1, 0]), buff=0.1, color=RED)
		text_vertex = Text("Node/Vertex", font="Lucida Console", font_size=30).next_to(arrow_to_vertex, LEFT)
		
		arrow_to_edge = Arrow(np.array([3, -2, 0]), np.array([1, -0.25, 0]), buff=0.1, color=GREEN)
		text_edge = Text("Edge", font="Lucida Console", font_size=30).next_to(arrow_to_edge, RIGHT)
		self.play(GrowArrow(arrow_to_vertex), Write(text_vertex))
		vertex_highlight = Circle(radius=0.314, color=RED, stroke_width=9).move_to(np.array([-1.69, 0.94, 0]))
		self.play(Create(vertex_highlight), run_time=1)
		self.wait(1)
		
		self.play(GrowArrow(arrow_to_edge), Write(text_edge))
		edge_highlight = Line(np.array([0, -0.47, 0]), np.array([2, 0.2, 0]), color=GREEN, stroke_width=8)
		self.play(Create(edge_highlight), run_time=1)

		self.play(FadeOut(vertex_highlight), FadeOut(edge_highlight), FadeOut(arrow_to_vertex), FadeOut(text_vertex), FadeOut(arrow_to_edge), FadeOut(text_edge))
		self.play(my_graph.animate.move_to(np.array([0, 2, 0])).scale(0.5))
		t3 = MarkupText(
			f"""
				<span fgcolor="{GREEN}">Graph Theory</span> allows us to analyze and model complex
			""",
			font="Lucida Console",
			font_size=30
		).move_to(ORIGIN)
		t31 = MarkupText(
			f"""
				<span fgcolor="{BLUE}">interconnected systems</span> across different fields.
			""",
			font="Lucida Console",
			font_size=30
		).next_to(t3, DOWN, buff=0)
		self.play(Write(t3), run_time=3)
		self.play(Write(t31), run_time=4)

		self.wait(1)
		self.play(FadeOut(t3), FadeOut(t31), run_time=0.5)
		
		self.play(my_graph.animate.move_to(ORIGIN).scale(1.5), run_time=1)
		self.wait(6)
		t4 = MarkupText(
			f"""
				<span fgcolor="{GREEN}">The degree</span> of a node.
			""",
			font="Lucida Console",
			font_size=30
		).next_to(my_graph, DOWN, buff=0.5)
		t41 = MarkupText(
			f"""
				Which is simply the <span fgcolor="{BLUE}">number of edges</span> connected to <span fgcolor="{YELLOW}">a single node</span>.
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t4, DOWN)
		self.play(Write(t4), run_time=2)
		self.play(Write(t41), run_time=4)
		self.wait(0.5)
		self.play(FadeOut(t4), FadeOut(t41), run_time=0.5)
		self.wait(1)
		edge_highlight2 = Line(np.array([-1.3, 0.75, 2.5]),np.array([0, -0.47, 2.5]), color=GREEN, stroke_width=10)
		self.play(Create(edge_highlight2), run_time=1)
		edge_highlight3 = Line(np.array([-1.3, 0.75, 2.5]),np.array([-1.77, -1.5, 2.5]), color=GREEN, stroke_width=10)
		self.play(Create(edge_highlight3), run_time=1)
		edge_highlight4 = Line(np.array([-1.3, 0.75, 2.5]),np.array([0.5, 1.35, 2.5]), color=GREEN, stroke_width=10)
		self.play(Create(edge_highlight4), run_time=1)
		self.wait(2)
		t5 = MarkupText(
			f"""
				Degrees of nodes:
			""",
			font="Lucida Console",
			font_size=25
		).move_to(np.array([4, -0.5, 0]))
		t51 = MarkupText(
			f"""
				Node 1: 1
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t5, DOWN, buff=0.25)
		t52 = MarkupText(
			f"""
				Node 2: 3
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t51, DOWN)
		t53 = MarkupText(
			f"""
				Node 3: 4
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t52, DOWN)
		t54 = MarkupText(
			f"""
				Node 4: 3
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t53, DOWN)
		t55 = MarkupText(
			f"""
				Node 5: 3
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t54, DOWN)
		t56 = MarkupText(
			f"""
				Node 6: 2
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t55, DOWN)
		self.play(Write(t5), run_time=0.5)
		self.play(Write(t52), run_time=1)
		self.wait(2)
		self.play(Write(t51), run_time=0.5)
		self.play(Write(t53), run_time=0.5)
		self.play(Write(t54), run_time=0.5)
		self.play(Write(t55), run_time=0.5)
		self.play(Write(t56), run_time=0.5)
		self.wait(2)
		self.play(FadeOut(t5), FadeOut(t51), FadeOut(t52), FadeOut(t53), FadeOut(t54), FadeOut(t55), FadeOut(t56), FadeOut(edge_highlight2), FadeOut(edge_highlight3), FadeOut(edge_highlight4), run_time=1)
		
		my_graph2 = MyGraph(node_positions, edges, labels, directed=True, graph_shift=shift)
		self.play(Create(my_graph2.vertices), run_time=3)
		self.play(Create(my_graph2.edge_lines), run_time=3)
		self.play(my_graph.animate.move_to(np.array([4, 0, 0])), run_time=1)
		self.play(my_graph2.animate.move_to(np.array([-4, 0, 0])), run_time=1)
		t6 = MarkupText(
			f"""
				Directed Graph
			""",
			font="Lucida Console",
			font_size=25
		).next_to(my_graph2, DOWN)
		t61 = MarkupText(
			f"""
				Undirected Graph
			""",
			font="Lucida Console",
			font_size=25
		).next_to(my_graph, DOWN)
		self.play(Write(t6), run_time=2)
		self.play(Write(t61), run_time=2)

		self.wait(5)
		self.play(FadeOut(t6), FadeOut(t61), FadeOut(my_graph2), run_time=1)
		self.play(my_graph.animate.move_to(np.array([0, 0, 0])), run_time=1)

		t7 = Text("Paths in a graph", font="Lucida Console", font_size=35).to_edge(UP, buff=0.2)
		self.play(Write(t7))
		self.wait(1)
		self.play(my_graph.animate.move_to(np.array([0, 1, 0])), run_time=1)

		t71 = MarkupText(
			f"""
			A <span fgcolor="{BLUE}">path</span> leads from a node to another through edges of the graph.
			""",
			font="Lucida Console",
			font_size=25
		).next_to(my_graph, DOWN, buff=0.2)
		t72 = MarkupText(
			f"""
			The <span fgcolor="{GREEN}">length</span> of a path is the number of edges in it.
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t71, DOWN, buff=0.2)
		self.play(Write(t71), run_time=3)
		self.play(Write(t72), run_time=3)
		self.wait(1)
		edge_highlight5 = Line(np.array([-1.77, -1.5+1, 2.5]), np.array([-1.3, 0.75+1, 2.5]), color=GREEN, stroke_width=10)
		edge_highlight6 = Line(np.array([-1.3, 0.75+1, 2.5]), np.array([0, -0.47+1, 2.5]), color=GREEN, stroke_width=10)
		edge_highlight7 = Line(np.array([0, -0.47+1, 0]), np.array([1.5, 0.2+1, 0]), color=GREEN, stroke_width=8)
		self.play(Create(edge_highlight5), run_time=1)
		self.play(Create(edge_highlight6), run_time=1)
		self.play(Create(edge_highlight7), run_time=1)
		t73 = MarkupText(
			f"""
			For instance, one path of this graph is:
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t72, DOWN, buff=0.2)
		t74 = MarkupText(
			f"""
			<span fgcolor="{BLUE}">1 -> 2 -> 4 -> 5</span>
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t73, DOWN, buff=0.2)
		t75 = MarkupText(
			f"""
			Its length is <span fgcolor="{GREEN}">3</span>.
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t74, DOWN, buff=0.2)
		self.play(Write(t73))
		self.play(Write(t74))
		self.play(Write(t75))
		self.wait(1)
		self.play(FadeOut(t71), FadeOut(t72), FadeOut(t73), FadeOut(t74), FadeOut(t75), FadeOut(edge_highlight5), FadeOut(edge_highlight6), FadeOut(edge_highlight7), run_time=1)
		self.wait(1)
		t76 = MarkupText(
			f"""
			A <span fgcolor="{RED}">cycle</span> is a path that starts and ends at the same node.
			""",
			font="Lucida Console",
			font_size=25
		).next_to(my_graph, DOWN, buff=0.2)
		edge_highlight8 = Line(np.array([-1.3, 0.75+1, 2.5]),np.array([0.5, 1.35+1, 2.5]), color=RED, stroke_width=10)
		edge_highlight11 = Line(np.array([0, -0.47+1, 2.5]), np.array([-1.3, 0.75+1, 2.5]), color=RED, stroke_width=10)
		edge_highlight10 = Line(np.array([1.5, 0.2+1, 0]),np.array([0, -0.47+1, 0]), color=RED, stroke_width=8)
		edge_highlight9 = Line(np.array([0.45, 1.35+1, 2.5]), np.array([1.5, 0.2+1, 0]), color=RED, stroke_width=8)
		self.play(Write(t76))
		self.play(Create(edge_highlight8), run_time=1)
		self.play(Create(edge_highlight9), run_time=1)
		self.play(Create(edge_highlight10), run_time=1)
		self.play(Create(edge_highlight11), run_time=1)
		
		t77 = MarkupText(
			f"""
			For instance, one path of this graph is:
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t76, DOWN, buff=0.2)
		t78 = MarkupText(
			f"""
			<span fgcolor="{BLUE}">2 -> 3 -> 5 -> 4 -> 2</span>
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t77, DOWN, buff=0.2)
		t79 = MarkupText(
			f"""
			Its length is <span fgcolor="{GREEN}">3</span>.
			""",
			font="Lucida Console",
			font_size=25
		).next_to(t78, DOWN, buff=0.2)
		self.play(Write(t77), run_time=1)
		self.play(Write(t78), run_time=1)
		self.play(Write(t79), run_time=1)
		self.wait(1)
		self.play(FadeOut(t76), FadeOut(t77), FadeOut(t78), FadeOut(t79), FadeOut(my_graph), FadeOut(edge_highlight8), FadeOut(edge_highlight9), FadeOut(edge_highlight10), FadeOut(edge_highlight11), run_time=1)


		node_positions2 = {
			"A": np.array([-2*2, 2*2-3, 0]), 
			"B": np.array([-1*2, 1*2-3, 0]), 
			"C": np.array([0*2, -1*2-3, 0]), 
			"D": np.array([0*2, 1*2-3, 0]),
			"E": np.array([2*2, 3*2-3, 0]),
		}
		edges2 = [
			("A", "B"),
			("B", "C"),
			("C", "D"),
			("D", "E"),
			("E", "A")
		]
		labels2 = {
			"A": "TS", 
			"B": "MS", 
			"C": "RM", 
			"D": "BH",
			"E": "HT",
		}

		shift = np.array([-0.9, 1.3, 0])
		my_graph3 = MyGraph(node_positions2, edges2, labels2, graph_shift=shift, vertex_radius=0.314)
		my_graph3.shift(RIGHT)
		my_graph3.shift(DOWN)
		self.play(Create(my_graph3.vertices), run_time=2)
		self.play(Create(my_graph3.edge_lines), run_time=2)
		self.wait(5)
