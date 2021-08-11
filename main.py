import random

def pass_gen(length=15):
	keylist = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
	login = []

	while len(login) < length:
		char = random.choice(keylist)
		login.append(char)

	return ''.join(login)

print('Ваш логин:', pass_gen())

def pass_gen2(length=15):
	keylist2 = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
	password = []

	while len(password) < length:
		char2 = random.choice(keylist2)
		password.append(char2)

	return ''.join(password)

print('Ваш пароль:', pass_gen2())