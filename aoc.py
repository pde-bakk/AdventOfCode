import datetime
import requests
import os
import sys


def get_input(day, year=datetime.datetime.today().year):
	url = f'https://adventofcode.com/{year}/day/{day}/input'
	if not os.environ['AOC_SESSION']:
		print('Please provide the env variable "AOC_SESSION" with your session token', file=sys.stderr)
		sys.exit(1)
	os.environ['AOC_SESSION'] = os.environ['AOC_SESSION'].replace('session=', '')
	r = requests.get(url=url, cookies={'session': os.environ['AOC_SESSION']})
	if r.status_code != requests.codes.ok:
		print(f"Can't retrieve the input file, unfortunately, status code = {r.status_code}", file=sys.stderr)
		sys.exit(2)
	content = r.content.decode('utf-8')
	return [x for x in content.splitlines()]


def get_todays_input_file():
	today = datetime.date.today()
	day, year = f'{today.day:02d}', str(today.year)
	with open(os.path.join(year, f'day{day}', 'input.txt'), 'w') as f:
		f.writelines('\n'.join(get_input(today.day, today.year)))


if __name__ == '__main__':
	get_todays_input_file()
