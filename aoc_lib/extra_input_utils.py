from typing import List


def split_on_double_newlines_instead(lines: List[str]) -> List[List[str]]:
	return [line.split('\n') for line in '\n'.join(lines).split('\n\n')]
