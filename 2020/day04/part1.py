valid = 0
passport = {}
with open("input") as myfile:
	for line in myfile:
		pairs = line.split()
		for p in pairs:
			key, value = p.partition(":")[::2]
			passport[key.strip()] = value
		if len(line) < 2:
			if "byr" in passport and "iyr" in passport and "eyr" in passport and "hgt" in passport and "hcl" in passport and "ecl" in passport and "pid" in passport:
				valid += 1
			passport = {}
print(valid)
