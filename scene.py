from manim import *
class GraphTheory(Scene):
	def construct(self):
		v = [1, 2, 3, 4, 5]
		e = [(1, 2), (1, 3), (1, 4), (3, 4), (2, 4), (2, 5), (4, 5)]
		g = Graph(v, e, labels=True, layout="planar")
		self.play(Create(g))
		self.wait()
		t1 = Text("What is that?", font="Lucida Console", font_size=38).shift(DOWN)
		self.play(g.animate.to_edge(UP, buff=0.2))
		self.play(Write(t1))
		self.play(t1.animate.next_to(g, buff=0.5))
		t2 = MarkupText(
			f"""
			This structure is called a <span fgcolor="{RED}">graph</span>.
			""",
			font="Lucida Console",
			font_size=32
		).next_to(g, DOWN, buff=0.5)
		t2_2 = MarkupText(
			f"""
			A graph is a <span fgcolor="{PURPLE}">structure</span> that visualizes
			<span fgcolor="{BLUE}">connections</span> between various <span fgcolor="{GREEN}">components</span>.
			""",
			font="Lucida Console",
			font_size=32
		).next_to(t2, DOWN, buff=0.2)
		self.play(Write(t2), run_time=2)
		self.wait()
		self.play(Write(t2_2), run_time=4)
		t3 = MarkupText(
			f"""
			  These components are called <span fgcolor="{GREEN}">nodes or vertices</span>,
			and the connections between them are called <span fgcolor="{BLUE}">edges</span>.
			""",
			font="Lucida Console",
			font_size=32
		).next_to(t2_2, DOWN, buff=0.5)
		self.wait()
		self.play(Write(t3), run_time=4)
		self.play(FadeOut(t1), FadeOut(t2), FadeOut(t2_2), FadeOut(t3))
		self.play(g.animate.move_to(ORIGIN))
		te = Text("Graph Terminology", font="Lucida Console").to_edge(UP, buff=0.2)
		self.play(Write(te))
		node = MarkupText(f'<span fgcolor="{GREEN}">Node</span>', font='Lucida Console').next_to(g, LEFT, buff=3)
		edge = MarkupText(f'<span fgcolor="{BLUE}">Edge</span>', font='Lucida Console').next_to(g, DOWN, buff=2)
		n1p = g.vertices[v.index(1) + 1].get_center()
		n1l = Text("1").move_to(n1p)
		a1 = Arrow(node, n1l)
		self.play(Create(node), Create(a1))
		self.wait()
		p1 = g.vertices[1].get_center()
		p2 = g.vertices[2].get_center()
		ed = p1 + (p2 - p1) / 2
		a2 = Arrow(edge, ed)
		self.play(Create(edge), Create(a2))
		self.wait()
