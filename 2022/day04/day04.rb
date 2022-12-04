require 'set'

f = File.readlines("input.txt", chomp: true)

part_1 = 0
part_2 = 0

f.each do |line|
	nbs = line.scan(/\d+/).map(&:to_i)
	set_1, set_2 = Set.new(nbs[0]..nbs[1]), Set.new(nbs[2]..nbs[3])
	if set_1.subset?(set_2) || set_1.superset?(set_2)
		part_1 += 1
	end
	if set_1.intersect?(set_2)
		part_2 += 1
	end
end

puts "Part 1: #{part_1}"
puts "Part 2: #{part_2}"
