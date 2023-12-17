NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)
NORTHWEST = (-1, -1)
NORTHEAST = (-1, 1)
SOUTHWEST = (1, -1)
SOUTHEAST = (1, 1)


def get_directions(diagonal: bool = False) -> list[tuple[int, int]]:
	directions = [SOUTH, NORTH, EAST, WEST]
	if diagonal:
		directions.extend([NORTHWEST, NORTHEAST, SOUTHWEST, SOUTHEAST])
	return directions


def get_direction_(direction: str) -> tuple[int, int]:
	directions = {
		'north': NORTH,
		'south': SOUTH,
		'east': EAST,
		'west': WEST,
		'southeast': SOUTHEAST,
		'southwest': SOUTHWEST,
		'northwest': NORTHWEST,
		'northeast': NORTHEAST
	}
	return directions[direction.lower()]


def yield_directions(diagonal: bool = False) -> tuple[int, int]:
	for direction in get_directions(diagonal=diagonal):
		yield direction


def add_directions(a: tuple[int, int], b: tuple[int, int]):
	return a[0] + b[0], a[1] + b[1]


def get_neighbours(y: int, x: int, diagonal: bool = False) -> list[tuple[int, int]]:
	return [(y + d[0], x + d[1]) for d in get_directions(diagonal=diagonal)]


def yield_neighbours(y: int, x: int, diagonal: bool = False) -> tuple[int, int]:
	for n in get_neighbours(y, x, diagonal):
		yield n
