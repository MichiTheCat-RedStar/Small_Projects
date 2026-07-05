#		RandLang // ☭
# MichiTheCat-RedStar (c) 2026

# Моя любовь к написанию кода в одну строку в совокупности с теорией об
# возможности случайно сыграть музыку не зная нот обезьяне... Шедевр!!!

from random import randint

if __name__ == '__main__': # вставьте свой код сюда
	CODE = '''
	if a == "Hello World!": print("And Goodbye!") # Сработает только если 'a' уже задана
	a = 1 # Тут показан пример, как может работать код, правда 'a' выполняет роль "Какая сейчас строка в рантайм?"
	print(a:="Hello World!" if a == 1 else None) # неизбежно сработает
	'''

def RandLang(your_code:str) -> None:
	run_codes = your_code.strip().split('\n')
	global_for_code, local_for_code = {}, {}
	while True:
		try:
			actual_code = run_codes.pop(randint(0, len(run_codes)-1)).strip()
		except ValueError:
			break
		try:
			exec(actual_code, global_for_code, local_for_code)
		except NameError:
			run_codes.append(actual_code)

if __name__ == '__main__':
	RandLang(CODE)
