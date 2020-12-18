import datetime
import requests
import os


def get_input(day, year=datetime.datetime.today().year):
	url = f'https://adventofcode.com/{year}/day/{day:02d}/input'
	r = requests.get(url=url, cookies={'session': os.environ['AOC_SESSION']})
	if r.status_code != requests.codes.ok:
		print(f"Can't retrieve the input file, unfortunately, status code = {r.status_code}")
		exit(2)
	content = r.content.decode('utf-8')
	return [x for x in content.splitlines()]

