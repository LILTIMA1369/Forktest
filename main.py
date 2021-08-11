8import random

def pass_gen(length=10):
	keylist = "01234567qwertyuiofghjklzxcvbnmQWERTYUASDFGHJKLZXCVBNM"
	password = []

	while len(password) < length:
		char = random.choice(keylist)
		password.append(char)

	return ''.join(password)

def log_gen(leng=8):
	loglist = "ASDFGHJKLXCVBNMERTYUIOwertyuiopcvbnmdfghjk"
	login = []

	while len(login) < leng:
		log = random.choice(loglist)
		login.append(log)

	return ''.join(login)	

a = pass_gen()
b = log_gen()
print(f'Ваш пароль: {a}, ваш логин: {b}')