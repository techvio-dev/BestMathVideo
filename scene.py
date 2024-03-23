from manim import *
class GraphTheory(Scene):
	def construct(self):
		no1 = "TS"
		no2 = "BH"
		no3 = "MD"
		no4 = "MS"
		no5 = "HT"
		v = [no1, no2, no3, no4, no5]
		e = [(no1, no2), (no2, no3), (no3, no4), (no4, no5), (no5, no1)]
		g = Graph(v, e, labels=True)
		self.play(Create(g), run_time=5)
		self.wait()
		t1 = Text("What is this?", font="Lucida Console", font_size=38).shift(DOWN * 2)
		self.play(g.animate.to_edge(UP, buff=0.5))
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
		self.play(Write(t2_2), run_time=4)
		t3 = MarkupText(
			f"""
			  These components are called <span fgcolor="{GREEN}">nodes or vertices</span>,
			and the connections between them are called <span fgcolor="{BLUE}">edges</span>.
			""",
			font="Lucida Console",
			font_size=32
		).next_to(t2_2, DOWN, buff=0.5)
		self.play(Write(t3), run_time=4)
