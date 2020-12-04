import re, string
valid = 0
passport = {}
eyecolours = "amb", "blu", "brn", "gry", "grn", "hzl", "oth"
with open("input") as myfile:
	for line in myfile:
		pairs = line.split()
		for p in pairs:
			key, value = p.partition(":")[::2]
			passport[key.strip()] = value
		if len(line) < 2:
			try:
				if "byr" not in passport or len(passport["byr"]) != 4 or not 1920 <= int(passport["byr"]) <= 2002:
					raise KeyError
				if "iyr" not in passport or len(passport["iyr"]) != 4 or not 2010 <= int(passport["iyr"]) <= 2020:
					raise KeyError
				if "eyr" not in passport or len(passport["eyr"]) != 4 or not 2020 <= int(passport["eyr"]) <= 2030:
					raise KeyError
				if "hgt" not in passport:
					raise KeyError
				else:
					res = re.findall(r'[A-Za-z]+|\d+', passport["hgt"])
					print(res)
					if not isinstance(res, list) or len(res) != 2 or (res[1] != "cm" and res[1] != "in"):
						print("height {} not valid".format(passport["hgt"]))
						raise KeyError
					if res[1] == "cm":
						if not 150 <= int(res[0]) <= 193:
							raise KeyError
					if res[1] == "in":
						if not 59 <= int(res[0]) <= 76:
							raise KeyError
				if "hcl" not in passport or not len(passport["hcl"]) == 7:
					raise KeyError
				else:
					if passport["hcl"][0] != '#':
						raise KeyError
					passport["hcl"] = passport["hcl"][1:]
					if not all(c in string.hexdigits for c in passport["hcl"]):
						raise KeyError
				if "ecl" not in passport or not any(col == passport["ecl"] for col in eyecolours):
					raise KeyError
				if "pid" not in passport or not len(passport["pid"]) == 9:
					raise KeyError
				print(res)
				valid += 1
			except (KeyError, ValueError) as e:
				pass
			passport = {}

print(valid)
