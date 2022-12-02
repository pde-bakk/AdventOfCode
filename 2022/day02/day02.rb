SCORES = {
	'A X' => 4,
	'A Y' => 8,
	'A Z' => 3,
	'B X' => 1,
	'B Y' => 5,
	'B Z' => 9,
	'C X' => 7,
	'C Y' => 2,
	'C Z' => 6,
}

CHOICES = {
	'A X' => 'Z',
	'A Y' => 'X',
	'A Z' => 'Y',
	'B X' => 'X',
	'B Y' => 'Y',
	'B Z' => 'Z',
	'C X' => 'Y',
	'C Y' => 'Z',
	'C Z' => 'X',
}

f = File.readlines("input.txt", chomp: true)
puts "Part 1: " + f.each.collect { |x| SCORES[x]}.sum.to_s
puts "Part 2: " + f.each.collect { |x| SCORES["#{x[0]} #{CHOICES[x]}"]}.sum.to_s
