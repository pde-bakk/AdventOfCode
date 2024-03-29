import requests
import os
import sys
import dotenv
from lxml.html import fromstring


def get_input_for_day(day: int, year: int) -> str:
	_ = dotenv.load_dotenv(dotenv.find_dotenv(), override=True)
	if 'AOC_SESSION' not in os.environ:
		print(f'Please provide a .env file with your AOC_SESSION token', file=sys.stderr)
		print(f'To find your token, check out this link: https://github.com/wimglenn/advent-of-code-wim/issues/1', file=sys.stderr)
		print(f'Example:\n$ cat .env\nAOC_SESSION=abcdef', file=sys.stderr)
		sys.exit(1)
	r = requests.get(url=f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': os.environ['AOC_SESSION']})
	if r.status_code != requests.codes.ok:
		print(f'Can\'t retrieve the input file, unfortunately, status code = {r.status_code}', file=sys.stderr)
		sys.exit(2)
	content = r.content.decode('utf-8')
	return content


def get_example_input(day: int, year: int) -> str:
	html = requests.get(url=f'https://adventofcode.com/{year}/day/{day}')
	soup = fromstring(html.text)
	elements = soup.xpath('/html/body/main/article[1]/pre/code/text()')
	if not elements:
		print(f'Can\'t retrieve the example.', file=sys.stderr)
		sys.exit(2)
	return elements[0]


def get_file(filename: str) -> str:
	*_, year, day = os.getcwd().split(os.path.sep)
	day = int(day.replace('day', ''))
	year = int(year)
	input_filename = os.path.join(os.getcwd(), filename)
	if os.path.exists(input_filename):
		with open(input_filename, 'r') as f:
			return f.read()
			# return f.read().splitlines()
	if filename == 'example.txt':
		input_lines = get_example_input(day, year)
	else:
		input_lines = get_input_for_day(day, year)
	with open(input_filename, 'w') as f:
		f.writelines(input_lines)
	return input_lines


def get_input_file() -> str:
	return get_file('input.txt')


def get_example_file() -> str:
	return get_file('example.txt')
