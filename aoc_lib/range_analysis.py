from dataclasses import dataclass
from typing import List


@dataclass
class RangeAnalysis:
	merged_ranges: List[range]
	unique_count: int
	total_count: int
	duplicate_count: int

	def __str__(self):
		return (f'Merged Ranges: {self.merged_ranges}\n'
				f'Unique Items: {self.unique_count}\n'
				f'Total Items (with duplicates): {self.total_count}\n'
				f'Duplicate Items: {self.duplicate_count}')


def analyze_ranges(ranges: List[range]) -> RangeAnalysis:
	if not ranges:
		raise ValueError("Range strings is empty")
	total_count = 0
	for r in ranges:
		total_count += len(r)

	merged_ranges = []
	unique_count = 0
	last_range = range(0, 0)

	for r in sorted(ranges, key=lambda x: x.start):
		if r.start in last_range:
			# Overlapping or adjacent range
			if r.stop > last_range.stop:
				unique_count += r.stop - last_range.stop
				last_range = range(last_range.start, r.stop)
		else:
			# Non-overlapping range - save previous and start new
			if last_range.start != last_range.stop:
				merged_ranges.append(range(last_range.start, last_range.stop))
			unique_count += len(r)
			last_range = r

	# Don't forget the last range
	if last_range.start != last_range.stop:
		merged_ranges.append(range(last_range.start, last_range.stop))
	duplicate_count = total_count - unique_count
	return RangeAnalysis(merged_ranges, unique_count, total_count, duplicate_count)


if __name__ == '__main__':
	result = analyze_ranges([range(3, 6), range(10, 15), range(16, 21), range(12, 19)])
	print(result)
	print(f'\nMerged: {result.merged_ranges}')
	assert result.unique_count == 14
