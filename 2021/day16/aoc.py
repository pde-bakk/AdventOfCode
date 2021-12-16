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
			print('bye')
			return 0
		self.subpackets = []
		self.version = int(binary[:3], 2)
		self.type_id = int(binary[3:6], 2)
		if self.version is None or self.type_id is None:
			print(f'version woulda been {binary[:3]}, type_id woulda been {binary[3:6]}')
		self.value = ''
		print(f'version={self.version}, type_id={self.type_id}')
		idx = 6
		if self.type_id == 4:  # Literal value
			firstbit = '1'
			while firstbit == '1':
				firstbit = binary[idx]
				label = binary[idx + 1: idx + 5]
				self.value += label
				idx += 5
				print(f'firstbit={firstbit}, label={label}, value={self.value}, idx={idx}')
			self.value = int(self.value, 2)
			print(f'setting value = {self.value}')
		else:  # Operator packet
			print(f'idx={idx}')
			self.length_type_id = int(binary[idx])
			idx += 1
			print(f'length_type_id={self.length_type_id}')
			if self.length_type_id == 0:
				self.total_bit_len = int(binary[idx:idx+15], 2)
				idx += 15
				target = idx + self.total_bit_len
				print(f'self.total_bitlen={self.total_bit_len}, end={target}, idx={idx}')
				print(f'subpackets={binary[idx:target]}')
				print(f'idx now is {idx}, binary[idx:]={binary[idx:]}')
				# exit(1)
				while idx < target:
					subpacket = Packet()
					print(f'{idx} < {target}')
					idx += subpacket.parse_packet(binary[idx:])
					print(f'new idx={idx}, binary[idx:]={binary[idx:]}')
					self.subpackets.append(subpacket)
			else:
				self.nb_subpackets = int(binary[idx:idx+11], 2)
				print(f'nb_subpackets ({binary[idx:idx+11]})={self.nb_subpackets}')
				idx += 11
				for _ in range(self.nb_subpackets):
					subpacket = Packet()
					idx += subpacket.parse_packet(binary[idx:])
					self.subpackets.append(subpacket)
		print(f'returning idx={idx}')
		return idx

	def get_versions(self) -> int:
		res = self.version
		print(f'Packet self has version: {self.version}, type_id: {self.type_id} and value {self.value}')
		for p in self.subpackets:
			# print(f'p has version: {p.version}, type_id: {p.type_id} and value {p.value}')
			tmp = p.get_versions()
			if tmp is not None:
				res += tmp
			# res += p.get_versions()
		return res

	def __str__(self) -> str:
		res = f'Packet with version {self.version} and type_id {self.type_id}\n'
		for p in self.subpackets:
			res += str(p)
		return res


puzzle_input = open('input.txt').read()
print(puzzle_input)
packets = []
binary_rep = bin(int(puzzle_input, 16)).lstrip('0b')
print(f'binary_rep used to be {binary_rep, len(binary_rep)}')
if len(binary_rep) % 4:
	binary_rep = '0' * (4 - len(binary_rep) % 4) + binary_rep
packet = Packet()
ret = packet.parse_packet(binary_rep)
print(packet.get_versions())
# print(str(packet))
