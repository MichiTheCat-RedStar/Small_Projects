#		cool_interface // ☭
# MichiTheCat-RedStar (c) 2026

from time import sleep


# display
def display(name:str, value_actual:int, value_max=100, display_size=30, end='\n', flush=False, symbols=('|', '.'), nums=False) -> None:
	'''Отображение полоски значения'''
	unit = display_size / value_max
	actual = value_actual
	value_actual = int(round(value_actual * unit))
	display = [symbols[1] for x in range(display_size)]
	for i in range(len(display)):
		if value_actual > 0:
			display[i] = symbols[0]
			value_actual -= 1
		else:
			break
	display = f'{name}: [{"".join(display)}] ({actual}/{value_max})' if nums else f'{name}: [{"".join(display)}]'
	print(display, end=end, flush=flush)

# draw
def draw(matrix:list, space=' ', transpose=False) -> None:
	'''Рисование карты или матрицы'''
	if transpose:
		for row in matrix:
			for cell in row:
				print(cell, end=space)
			print()
	else:
		for cell in range(len(matrix[0])):
			for row in range(len(matrix)):
				print(matrix[row][cell], end=space)
			print()

'''
def table(matrix:list) -> None:
	max_size = 1
	for row in matrix:
		for cell in row:
			size = len(cell)
			if size > max_size:
				max_size = size
	for row in matrix:
		for cell in row:
			print()
			size = len(cell)
			if size > max_size:
				max_size = size''' # TODO: сделать вывод таблиц, чтобы они выводились ровно, умножая пробел, чтобы все были одного размера


# Test
if __name__ == '__main__':
	print('- display test -')
	display('MIN', 0, nums=True)
	display('MAX', 100, nums=True, end='\n\n')
	display('HP', 10)
	display('Energy', 25, display_size=26)
	for i in range(51):
		display('Loading', i, value_max=50, display_size=25, end='\r', flush=True, nums=True)
		sleep(0.05)

	print('\n\n- draw test -')
	draw([['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']], transpose=False)
	print()
	draw([['00', '01', '02'], ['10', '11', '12'], ['20', '21', '22']], transpose=True)
