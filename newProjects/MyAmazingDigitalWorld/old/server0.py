#		MADW/server // ☭
# MichiTheCat-RedStar (c) 2026

import asyncio

IP = None
PORT = None

# TEST
IP = '127.0.0.1'
PORT = 2077

async def client():
	global IP, PORT
	print('MichiTheCat-RedStar (c) 2026\nДобро пожаловать в серверную часть MyAmazingDigitalWorld!')
	print('\nIP и порт не заданы...' if (IP == None) and (PORT == None) else '')
	while True: # Ввод IP и PORT, если они не введены
		try:
			if IP == None:
				IP = input('\nВведите IP: ').strip()
			if PORT == None:
				PORT = int(input('Введите порт: '))
			root, root = asyncio.open_connection('')
		except Exception as e:
			print('\nОшибка:', e)
			IP, PORT = None, None
		else:
			break

	root.write(('Привет!\n').encode())
	resp = await root.readline()
	print(resp.decode())

asyncio.run(client())
