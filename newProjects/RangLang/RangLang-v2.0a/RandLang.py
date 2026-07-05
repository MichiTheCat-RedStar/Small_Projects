#		RandLang // ☭
# MichiTheCat-RedStar (c) 2026

# Моя любовь к написанию кода в одну строку в совокупности с теорией об
# возможности случайно сыграть музыку не зная нот обезьяне... Шедевр!!!

from random import randint
import re


def RandLang(your_code:str) -> None:
	# Нарезаю строки
	run_codes = your_code.strip().split('\n')
	
	# Обработка последовательности
	new_codes = []
	delet = []
	sequence_buffer = {'line':-1, 'content':[]}
	
	def clear_buffer():
		nonlocal sequence_buffer, new_codes
		new_codes.append('\n'.join(sequence_buffer['content']))
		sequence_buffer = {'line':-1, 'content':[]}
	
	for actual_code_index in range(0, len(run_codes)):
		sequence = {'line':re.match(r'[0-9]*;', run_codes[actual_code_index]),
					'content': run_codes[actual_code_index]}
		if sequence['line']:
			sequence['line'] = int(sequence['line'].group()[:-1])
			if sequence_buffer['line'] < sequence['line']:
				sequence_buffer['line'] = sequence['line']
				sequence_buffer['content'].append(run_codes[actual_code_index][len(str(sequence['line']))+1:])
			else:
				clear_buffer()
				new_codes.append(run_codes.pop(actual_code_index))  # заменить pop на delete
		else:
			clear_buffer()
			new_codes.append(run_codes.pop(actual_code_index)) # заменить pop на delete
	run_codes = new_codes
	
	# Исполняю строки
	code_args = {}, {}
	while True:
		try:
			actual_code = run_codes.pop(randint(0, len(run_codes)-1)).strip()
		except ValueError:
			break
		try:
			exec(actual_code, *code_args)
		except NameError:
			run_codes.append(actual_code)


if __name__ == '__main__':
	RandLang('''
0;if a:
1;    print(a)
a = 'Hello World!'
0;if a:
1;    print('World Hello!')
	''')
