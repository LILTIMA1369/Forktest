import random 
import time

def pass_gen(length=15):
	keylist = "0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
	password = []

	while len(password) < length:
		char = random.choice(keylist)
		password.append(char)

	print(''.join(password))

print(pass_gen())

while True:
	pass_gen()
	time.sleep(5)

# from crontab import CronTab
# cron = CronTab(user='User')
# job = cron.new(command='pass_gen')
# job.minute.every(1)
# cron.write()