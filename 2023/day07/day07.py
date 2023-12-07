import functools
import sys
import math

sys.path.append('../..')
from aoc_lib.get_input import get_input_file, get_example_file
from aoc_lib.utilities import *
from aoc_lib.extra_input_utils import split_on_double_newlines_instead

p2_flag = False


def compare(card_a: tuple[str, str, int], card_b: tuple[str, str, int]):
	hand_a, orig_a, _ = card_a
	hand_b, orig_b, _ = card_b
	card_strengths = '23456789TJQKA'
	if p2_flag:
		card_strengths = 'J23456789TQKA'
	counts_a = [hand_a.count(c) for c in hand_a]
	counts_b = [hand_b.count(c) for c in hand_b]
	if counts_a.count(5) != counts_b.count(5):
		print(f'5. {hand_a} > {hand_b}')
		return [-1, 1][counts_a.count(5) > counts_b.count(5)]
	if counts_a.count(4) != counts_b.count(4):
		print(f'4. {hand_a} > {hand_b}')
		return [-1, 1][counts_a.count(4) > counts_b.count(4)]
	if int(3 in counts_a and 2 in counts_a) != int(3 in counts_b and 2 in counts_b):
		print(f'FH. {hand_a} > {hand_b}')
		return [-1, 1][int(3 in counts_a and 2 in counts_a) > int(3 in counts_b and 2 in counts_b)]
	if counts_a.count(3) != counts_b.count(3):
		print(f'3. {hand_a} > {hand_b}, {counts_a.count(3)} vs {counts_b.count(3)}')
		return [-1, 1][counts_a.count(3) > counts_b.count(3)]
	if counts_a.count(2) != counts_b.count(2):  # Maybe wrong
		print(f'2. {hand_a} > {hand_b}')
		return [-1, 1][counts_a.count(2) > counts_b.count(2)]
	for a, b in zip(orig_a, orig_b):
		if a != b:
			print(f'idx. {hand_a} {"<>"[card_strengths.index(a) > card_strengths.index(b)]} {hand_b}, cus {card_strengths.index(a)} vs {card_strengths.index(b)}')
			print(f'{orig_a=}, {orig_b=}, {a,b=}')
			return [-1, 1][card_strengths.index(a) > card_strengths.index(b)]
	print(f'SHOULDNT HAPPEN. {hand_a} == {hand_b}')
	return 0


def get_scores(hand: str):
	counts = [hand.count(c) for c in hand]
	return [counts.count(i) for i in [5, 4, 3, 2]]


def make_best_joker_hand(hand: str) -> str:
	card_strengths = 'J23456789TQKA'
	if 'J' not in hand:
		return hand
	arr = []
	for replacement in card_strengths[1:]:
		new_hand = hand.replace('J', replacement)
		arr.append((get_scores(new_hand), new_hand))
	best = max(arr)
	print(f'For {hand=}, joker is best used to make the hand {best}')
	return best[1]


def aoc(lines: list[str], prefix: str) -> None:
	part1 = 0
	part2 = 0
	cards = []
	for hand, bid in map(str.split, lines):
		bid = int(bid)
		print(hand, bid)
		cards.append((hand, hand, bid))
	cards.sort(key=functools.cmp_to_key(compare))
	print(cards)
	part1 = sum([bid * idx for idx, (hand, og_hand, bid) in enumerate(cards, start=1)])
	print(f'{prefix} part 1: {part1}')
	global p2_flag
	p2_flag = True
	for i, (hand, hand, bid) in enumerate(cards):
		cards[i] = make_best_joker_hand(hand), hand, bid
	cards.sort(key=functools.cmp_to_key(compare))
	print(cards)
	part2 = sum([bid * idx for idx, (hand, _, bid) in enumerate(cards, start=1)])
	print(f'{prefix} part 2: {part2}')


if __name__ == '__main__':
	aoc(get_example_file(), 'Example')
	aoc(get_input_file(), 'Solution')
