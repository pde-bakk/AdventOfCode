from .directions import *


def shoelace(points: list[Position], include_line: bool = True) -> int:
	area = 0
	for a, b in zip(points, points[1:]):
		area += (b.x + a.x) * (b.y - a.y)
	if include_line:
		return (abs(area) + len(points)) // 2 + 1
	return abs(area) // 2
