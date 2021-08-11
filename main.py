import random

def pass_gen(length=15):
	keylist = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
	password = []

	while len(password) < length:
		char = random.choice(keylist)
		password.append(char)

	return ''.join(password)
	

print(pass_gen())


login = ''
for x in range(8): 
    login = login + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFOGHIGKLMNOPQRSTUVYXWZ')) 
print(login)



