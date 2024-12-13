from typing import Any


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

	def isvalid(self, len_y: int, len_x: int) -> bool:
		return 0 <= self.y < len_y and 0 <= self.x < len_x

	def checkvalid(self, griddy: list[list[Any]]) -> bool:
		return 0 <= self.y < len(griddy) and 0 <= self.x < len(griddy[0])

	def __str__(self) -> str:
		return f'Pos(y={self.y}, x={self.x})'

	def __repr__(self):
		return f'Position(y={self.y}, x={self.x})'

	def __eq__(self, other):
		if not isinstance(other, Position):
			return NotImplemented
		return (self.y, self.x) == (other.y, other.x)

	def __hash__(self):
		return hash((self.y, self.x))
		# return self.y, self.x


class Direction(Position):
	def __init__(self, y: int, x: int, normalized: bool = False):
		super().__init__(y, x)
		if normalized:
			assert abs(y) <= 1 and abs(x) <= 1

	@staticmethod
	def get_directions(diagonal: bool = False) -> list['Direction']:
		directions = [SOUTH, NORTH, EAST, WEST]
		if diagonal:
			directions.extend([NORTHWEST, NORTHEAST, SOUTHWEST, SOUTHEAST])
		return directions

	def __str__(self) -> str:
		dmap = {
			NORTH: 'NORTH',
			SOUTH: 'SOUTH',
			WEST: 'WEST',
			EAST: 'EAST',
		}
		return dmap[self]

	def __repr__(self):
		return self.__str__()
		# return f'Direction(y={self.y}, x={self.x})'

	def __mul__(self, other):
		if not isinstance(other, int):
			return NotImplemented
		return Position(self.y * other, self.x * other)

	def __rmul__(self, other):
		return self * other
		# if not isinstance(other, int):
		# 	return NotImplemented
		# return self * other

	def turn_right(self) -> 'Direction':
		directions = [WEST, SOUTH, EAST, NORTH]
		assert self in directions
		return directions[directions.index(self) - 1]

	def turn_left(self) -> 'Direction':
		directions = [NORTH, EAST, SOUTH, WEST]
		assert self in directions
		return directions[directions.index(self) - 1]

NORTH = Direction(-1, 0)
SOUTH = Direction(1, 0)
EAST = Direction(0, 1)
WEST = Direction(0, -1)
NORTHWEST = Direction(-1, -1)
NORTHEAST = Direction(-1, 1)
SOUTHWEST = Direction(1, -1)
SOUTHEAST = Direction(1, 1)


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

