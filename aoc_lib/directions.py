class Position:
	def __init__(self, y: int, x: int):
		if not isinstance(y, int) or not isinstance(x, int):
			raise NotImplementedError
		self.y, self.x = y, x

	def __abs__(self):
		return Position(abs(self.y), abs(self.x))

	def __add__(self, other):
		if not isinstance(other, Position):
			return NotImplemented
		return Position(self.y + other.y, self.x + other.x)

	def __mul__(self, other):
		if not isinstance(other, int):
			return NotImplemented
		return Position(self.y * other, self.x * other)

	def __lt__(self, other):
		if not isinstance(other, Position):
			return NotImplemented
		return (self.y, self.x) < (other.y, other.x)

	def __iadd__(self, other):
		return self + other

	def __sub__(self, other):
		if not isinstance(other, Position):
			return NotImplemented
		return Position(self.y - other.y, self.x - other.x)

	def get_neighbours(self, diagonal: bool = False):
		for direction in [NORTH, SOUTH, EAST, WEST]:
			yield self + direction
		if diagonal:
			for direction in [NORTHWEST, NORTHEAST, SOUTHWEST, SOUTHEAST]:
				yield self + direction

	def __str__(self) -> str:
		return f'Position(y={self.y}, x={self.x})'

	def __repr__(self):
		return str(self)

	def __eq__(self, other):
		if not isinstance(other, Position):
			return NotImplemented
		return (self.y, self.x) == (other.y, other.x)

	def __hash__(self):
		return hash((self.y, self.x))
		# return self.y, self.x



NORTH = Position(-1, 0)
SOUTH = Position(1, 0)
EAST = Position(0, 1)
WEST = Position(0, -1)
NORTHWEST = Position(-1, -1)
NORTHEAST = Position(-1, 1)
SOUTHWEST = Position(1, -1)
SOUTHEAST = Position(1, 1)


# def get_directions(diagonal: bool = False) -> list[tuple[int, int]]:
# 	directions = [SOUTH, NORTH, EAST, WEST]
# 	if diagonal:
# 		directions.extend([NORTHWEST, NORTHEAST, SOUTHWEST, SOUTHEAST])
# 	return directions


# def get_direction_(direction: str) -> tuple[int, int]:
# 	directions = {
# 		'north': NORTH,
# 		'south': SOUTH,
# 		'east': EAST,
# 		'west': WEST,
# 		'southeast': SOUTHEAST,
# 		'southwest': SOUTHWEST,
# 		'northwest': NORTHWEST,
# 		'northeast': NORTHEAST
# 	}
# 	return directions[direction.lower()]


# def yield_directions(diagonal: bool = False) -> tuple[int, int]:
# 	for direction in get_directions(diagonal=diagonal):
# 		yield direction
#
#
# def add_directions(a: tuple[int, int], b: tuple[int, int]):
# 	return a[0] + b[0], a[1] + b[1]
#
#
# def get_neighbours(y: int, x: int, diagonal: bool = False) -> list[tuple[int, int]]:
# 	return [(y + d[0], x + d[1]) for d in get_directions(diagonal=diagonal)]
#
#
# def yield_neighbours(y: int, x: int, diagonal: bool = False) -> tuple[int, int]:
# 	for n in get_neighbours(y, x, diagonal):
# 		yield n
