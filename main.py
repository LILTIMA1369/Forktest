
import random 
import time



# Генератор поролей
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

def pass_gen(length=10):
	keylist = "01234567qwertyuiofghjklzxcvbnmQWERTYUASDFGHJKLZXCVBNM"

	password = []

	while len(password) < length:
		char2 = random.choice(keylist2)
		password.append(char2)


	print(''.join(password))

print(pass_gen())

while True:
	pass_gen()
	time.sleep(5)

	return ''.join(password)
	

print(pass_gen())

# Генератор логина

login = ''
for x in range(8): 
    login = login + random.choice(list('1234567890abcdefghigklmnopqrstuvyxwzABCDEFOGHIGKLMNOPQRSTUVYXWZ')) 
print(login)





print('Ваш пароль:', pass_gen2())


print(pass_gen())


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


