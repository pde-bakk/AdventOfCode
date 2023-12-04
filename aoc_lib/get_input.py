import datetime
import requests
import os
import sys
import dotenv
from lxml.html import fromstring


def fetch_url_content(url: str) -> str:
	dotenv.load_dotenv('../../.env')
	if not os.environ['AOC_SESSION']:
		print('Please provide the env variable "AOC_SESSION" with your session token', file=sys.stderr)
		sys.exit(1)
	os.environ['AOC_SESSION'] = os.environ['AOC_SESSION'].replace('session=', '')
	r = requests.get(url=url, cookies={'session': os.environ['AOC_SESSION']})
	print(r.json())
	if r.status_code != requests.codes.ok:
		print(f"Can't retrieve the input file, unfortunately, status code = {r.status_code}", file=sys.stderr)
		sys.exit(2)
	content = r.content.decode('utf-8')
	return content


def get_input_for_day(day: int, year: int) -> str:
	dotenv.load_dotenv('../../.env')
	if not os.environ['AOC_SESSION']:
		print('Please provide the env variable "AOC_SESSION" with your session token', file=sys.stderr)
		sys.exit(1)
	os.environ['AOC_SESSION'] = os.environ['AOC_SESSION'].replace('session=', '')
	r = requests.get(url=f'https://adventofcode.com/{year}/day/{day}/input', cookies={'session': os.environ['AOC_SESSION']})
	print(r.json())
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


def get_input_file() -> list[str]:
	*_, year, day = os.getcwd().split(os.path.sep)
	day = int(day.replace('day',''))
	input_filename = os.path.join(os.getcwd(), 'input.txt')
	if os.path.exists(input_filename):
		with open(input_filename, 'r') as f:
			return f.read().splitlines()
	input_lines = get_input_for_day(day, year)
	with open(input_filename, 'w') as f:
		f.writelines(input_lines)
	return input_lines.splitlines()


def get_example_file() -> list[str]:
	*_, year, day = os.getcwd().split(os.path.sep)
	day = int(day.replace('day',''))
	example_filename = os.path.join(os.getcwd(), 'example.txt')
	if os.path.exists(example_filename):
		with open(example_filename, 'r') as f:
			return f.read().splitlines()
	input_lines = get_example_input(day, year)
	with open(example_filename, 'w') as f:
		f.writelines(input_lines)
	return input_lines.splitlines()
