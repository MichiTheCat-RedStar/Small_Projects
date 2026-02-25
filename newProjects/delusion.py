from random import choice as ra
from time import sleep as sl
try: slap = float(input('float> '))
except: print('Wrong! Set 0.1'); slap = 0.1
while True:
	print(ra(['\b ', '#', '\b', '\b#']), end='', flush=True)
	sl(slap)
