import sys
import math
import networkx as nx
import matplotlib.pyplot as plt


sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import *
from aoc_lib.directions import *


def parse(data: str) -> nx.Graph:
	g = nx.Graph()
	for line in split_data_on_newlines(data):
		name, *components = line.replace(':', '').split()
		g.add_node(name)
		for comp in components:
			g.add_node(comp)
			g.add_edge(name, comp)
	return g


def solve(g: nx.Graph) -> int:
	# nx.draw(g, with_labels=True)
	# plt.show()
	g.remove_edges_from(nx.minimum_edge_cut(g))
	lengths = [len(subgraph) for subgraph in nx.connected_components(g)]
	return math.prod(lengths)


def aoc(data: str, prefix: str) -> None:
	mapping = parse(data)
	part1 = solve(mapping)
	print(f'{prefix} part 1: {part1}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
