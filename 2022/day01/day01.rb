f = File.open('input.txt', 'r')
elfs = f.read.split("\n\n")
sums = elfs.each.collect {|x| x.split.map(&:to_i).sum}.sort
puts sums.max
puts sums[-3..].sum
