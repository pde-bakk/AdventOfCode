from hashlib import md5
secret = "bgvyzdsv"
for i in range(999999999999):
	answer = md5((secret + str(i)).encode()).hexdigest()
	if answer[:6] == '000000':
		print(answer)
		print(i)
		break