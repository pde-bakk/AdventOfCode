import functools
import sys

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file

p2_flag = False


def get_score(hand: str):
	counts = [hand.count(c) for c in hand]
	return [counts.count(i) for i in [5, 4, 3, 2]]


def compare(card_a: tuple[str, str, int], card_b: tuple[str, str, int]):
	hand_a, orig_a, _ = card_a
	hand_b, orig_b, _ = card_b
	card_strengths = ['23456789TJQKA', 'J23456789TQKA'][p2_flag]
	for a, b in zip(get_score(hand_a), get_score(hand_b)):
		if a != b:
			return [-1, 1][a > b]
	for a, b in zip(orig_a, orig_b):
		if a != b:
			return [-1, 1][card_strengths.index(a) > card_strengths.index(b)]
	return 0


def make_best_joker_hand(hand: str) -> str:
	card_strengths = 'J23456789TQKA'
	if 'J' not in hand:
		return hand
	arr = [(get_score(new_hand), new_hand) for replacement in card_strengths[1:] if (new_hand := hand.replace('J', replacement))]
	return max(arr)[1]


def aoc(lines: list[str], prefix: str) -> None:
	def calculate_winnings(x) -> int:
		return sum([bid * idx for idx, (hand, og_hand, bid) in enumerate(x, start=1)])
	global p2_flag
	p2_flag = False
	cards = [(hand, hand, int(bid)) for hand, bid in map(str.split, lines)]
	cards.sort(key=functools.cmp_to_key(compare))
	print(f'{prefix} part 1: {calculate_winnings(cards)}')

	p2_flag = True
	for i, (hand, hand, bid) in enumerate(cards):
		cards[i] = make_best_joker_hand(hand), hand, bid
	cards.sort(key=functools.cmp_to_key(compare))
	print(f'{prefix} part 2: {calculate_winnings(cards)}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
