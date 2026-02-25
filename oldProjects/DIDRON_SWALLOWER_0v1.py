from random import randint

print("WELCOME TO DIDRON SWALLOWER!")

check = False

def Ping():
	return("PONG")
	
def Help():
	return("[NOT AVAILABLE]")
	
def Check():
	global check
	if check:
		check = False
		return("FALSE NOW")
	else:
		check = True
		return("TRUE NOW")
		
def Gelp():
	return(randint(0, 9))

def Version(): # VERSION VERSION VERSION
	return("0.1")

while True:
	User = input("\n> ").lower()
	if User == "ping": print(Ping())
	elif User == "help": print(Help())
	elif User == "check": print(Check())
	elif User == "gelp": print(Gelp())
	elif User == "version": print(Version())
	
	elif check:
		print("MISSING")