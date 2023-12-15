def split_data_on_newlines(data: str) -> list[str]:
	return data.splitlines()


def split_on_double_newlines(data: str) -> list[list[str]]:
	return [segment.splitlines() for segment in data.split('\n\n')]


# def split_on_double_newlines_instead(lines: List[str]) -> List[List[str]]:
# 	return [line.split('\n') for line in '\n'.join(lines).split('\n\n')]
