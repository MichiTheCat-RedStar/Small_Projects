#		Chat/client // ☭
# MichiTheCat-RedStar (c) 2026

import asyncio

IP = '127.0.0.1'
PORT = 2077

print('MichiTheCat-RedStar (c) 2026\nДобро пожаловать в Chat-MyAmazingDigitalWorld!\n')

Name = input('Введите свой ник: ')

async def reader(reader):
	while True:
		data = await reader.read(1024)
		if not data:
			break
		print(data.decode())

async def main():
	reader, writer = await asyncio.open_connection(IP, PORT)
	print('Сервер подключен')
	while True:
		message = f'{Name}: '+input('\nВведите сообщение: ')
		writer.write(message.encode('utf-8'))
		await writer.drain()
		asyncio.run(reader(reader))
		print(answer.decode('utf-8'))

print('\nПодключение к серверу...')
asyncio.run(main())
