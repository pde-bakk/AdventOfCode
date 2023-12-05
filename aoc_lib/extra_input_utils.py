def split_on_double_newlines_instead(lines: list[str]) -> list[str]:
	return '\n'.join(lines).split('\n\n')
