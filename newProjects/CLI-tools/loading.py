#		loading // ☭
# MichiTheCat-RedStar (c) 2026

from time import sleep


# loading
def loading(text='Загрузка...', animation=0) -> str:
	'''Анимация загрузки
	text - текст перед анимацией
	animation:
	 0  - крутящаяся палочка
	 1  - точки
	 2  - луна (emoji)
	 3  - квадрат
	 4  - квадрат волна
	 5  - прямоугольник
	 6  - прямоугольник волна
	 7  - сирена
	 8  - жук
	 9  - буглый круг
	 10 - беглый квадрат
	 11 - пиксель'''
	
	match animation:
		case 0:
			symbols=['\\', '|', '/', '-']
		case 1:
			symbols=['.   ', '..  ', '... ', '....']
		case 2:
			symbols=['🌕', '🌖', '🌗', '🌘', '🌑', '🌒', '🌓', '🌔']
		case 3:
			symbols=['▏', '▎', '▍', '▌', '▋', '▊', '▉', '█']
		case 4:
			symbols=['▏', '▎', '▍', '▌', '▋', '▊', '▉', '█',
				'█', '▉', '▊', '▋', '▌', '▍', '▎']
		case 5:
			symbols=['▁', '▂', '▃', '▄', '▅', '▆', '▇', '█']
		case 6:
			symbols=['▁', '▃', '▅','▇', '█', '▇', '▅', '▃']
		case 7:
			symbols=['◐', '◑']
		case 8:
			symbols=['▖', '▘', '▝', '▗']
		case 9:
			symbols=['◴', '◵', '◶', '◷']
		case 10:
			symbols=['◰', '◱', '◲', '◳']
		case 11:
			symbols=['⠁', '⠈', '⠐', '⠠', '⢀', '⡀', '⠄', '⠂']
		#TODO: тут можно ещё делать и делать... Особенно меня удивил
		#      шрифт Брайля - это же массив 2x4 размером с один символ -
		#      идеал для фантазий в пиксель-арте!
	
	index = 0
	while True:
		yield f'{text} {symbols[index]}'
		index = (index + 1) % len(symbols)


# Test
if __name__ == '__main__':
	print('- Test -')
	animation = loading()
	for _ in range(20):
		print(next(animation), end='\r', flush=True)
		sleep(0.1)
	
	print()
	animation = loading('Соединение', 1)
	for _ in range(15):
		print(next(animation), end='\r', flush=True)
		sleep(0.25)
	
	print()
	animation = loading('Телескопия:', 2)
	for _ in range(20):
		print(next(animation), end='\r', flush=True)
		sleep(0.15)
	
	print()
	animation = loading('Квадрат:', 3)
	for _ in range(25):
		print(next(animation), end='\r', flush=True)
		sleep(0.1)
	
	print()
	animation = loading('Лёгкое:', 4)
	for _ in range(50):
		print(next(animation), end='\r', flush=True)
		sleep(0.05)
	
	print()
	animation = loading('Фортнайт:', 5)
	for _ in range(12):
		print(next(animation), end='\r', flush=True)
		sleep(0.26)
	
	print()
	animation = loading('Пирамида:', 6)
	for _ in range(40):
		print(next(animation), end='\r', flush=True)
		sleep(0.08)
	
	print()
	animation = loading('Таракан:', 7)
	for _ in range(8):
		print(next(animation), end='\r', flush=True)
		sleep(0.42)
	
	print()
	animation = loading('Жучара:', 8)
	for _ in range(16):
		print(next(animation), end='\r', flush=True)
		sleep(0.20)
	
	print()
	animation = loading('круг:', 9)
	for _ in range(16):
		print(next(animation), end='\r', flush=True)
		sleep(0.20)
	
	print()
	animation = loading('некруг:', 10)
	for _ in range(16):
		print(next(animation), end='\r', flush=True)
		sleep(0.20)
	
	print()
	animation = loading('Брайль:', 11)
	for _ in range(64):
		print(next(animation), end='\r', flush=True)
		sleep(0.06)

