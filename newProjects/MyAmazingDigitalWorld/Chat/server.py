#		Chat/server // ☭
# MichiTheCat-RedStar (c) 2026

import asyncio

IP = '127.0.0.1'
PORT = 2077

print('MichiTheCat-RedStar (c) 2026\nДобро пожаловать в серверную часть Chat-MyAmazingDigitalWorld!\n')

Clients = []
async def handle_client(reader, writer):
	Clients.append(writer)
	while True:
		data = await reader.read(1024)
		if not data: break
		print(data.decode('utf-8'))
		for w in Clients:
			if w != writer:
				w.write(data)
				await w.drain()


async def main():
	server = await asyncio.start_server(handle_client, IP, PORT)
	print('Сервер запущен.')
	async with server:
		await server.serve_forever()

asyncio.run(main())
