from functools import reduce


class Packet:
	def __init__(self):
		self.type_id = None
		self.nb_subpackets = None
		self.total_bit_len = None
		self.length_type_id = None
		self.value = 0
		self.version = None
		self.subpackets = []

	def parse_packet(self, binary: str):
		print(f'parse_packet: binary={binary}')
		if not binary:
			return 0
		self.subpackets = []
		self.version = int(binary[:3], 2)
		self.type_id = int(binary[3:6], 2)
		idx = 6
		if self.type_id == 4:  # Literal value
			idx = self.parse_literal(binary, idx)
		else:  # Operator packet
			idx = self.extract_operator(binary, idx)
		return idx

	def extract_operator(self, binary, idx):
		self.length_type_id = int(binary[idx])
		idx += 1
		if self.length_type_id == 0:
			self.total_bit_len = int(binary[idx:idx + 15], 2)
			idx += 15
			target = idx + self.total_bit_len
			while idx < target:
				subpacket = Packet()
				idx += subpacket.parse_packet(binary[idx:])
				self.subpackets.append(subpacket)
		else:
			self.nb_subpackets = int(binary[idx:idx + 11], 2)
			idx += 11
			for _ in range(self.nb_subpackets):
				subpacket = Packet()
				idx += subpacket.parse_packet(binary[idx:])
				self.subpackets.append(subpacket)
		return idx

	def parse_literal(self, binary, idx):
		firstbit = '1'
		self.value = ''
		while firstbit == '1':
			firstbit = binary[idx]
			label = binary[idx + 1: idx + 5]
			self.value += label
			idx += 5
		self.value = int(self.value, 2)
		return idx

	def get_versions(self) -> int:
		res = self.version
		for p in self.subpackets:
			tmp = p.get_versions()
			if tmp is not None:
				res += tmp
		return res

	def __lt__(self, other):
		return self.getvalue() < other.getvalue()

	def __gt__(self, other):
		return self.getvalue() > other.getvalue()

	def __eq__(self, other):
		return self.getvalue() == other.getvalue()

	def getvalue(self) -> int:
		match self.type_id:
			case 0:
				return sum([p.getvalue() for p in self.subpackets])
			case 1:
				res = 1
				for item in self.subpackets:
					res *= item.getvalue()
				return res
				# return reduce(lambda x, y: x.getvalue() * y.getvalue(), self.subpackets)
			case 2:
				return min(self.subpackets).getvalue()
			case 3:
				return max(self.subpackets).getvalue()
			case 4:
				return self.value
			case 5:
				return int(self.subpackets[0] > self.subpackets[1])
			case 6:
				return int(self.subpackets[0] < self.subpackets[1])
			case 7:
				return int(self.subpackets[0] == self.subpackets[1])
			case _:
				return 0


puzzle_input = open('input.txt').read()
binary_rep = bin(int(puzzle_input, 16)).lstrip('0b')
if len(binary_rep) % 4:
	binary_rep = '0' * (4 - len(binary_rep) % 4) + binary_rep
if puzzle_input[0] == '0':
	binary_rep = '0' * 4 + binary_rep
packet = Packet()
ret = packet.parse_packet(binary_rep)
print(f'Part1: {packet.get_versions()}')
print(f'Part2: {packet.getvalue()}')
