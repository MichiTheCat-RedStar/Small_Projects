#		MADW/server // ☭
# MichiTheCat-RedStar (c) 2026

import asyncio

IP = '127.0.0.1'
PORT = 2077

print('MichiTheCat-RedStar (c) 2026\nДобро пожаловать в серверную часть MyAmazingDigitalWorld!\n')

async def handle_client(reader, writer):
	data = await reader.read(1024)
	print(data)
	writer.close()
	await writer.wait_closed()

async def main():
	server = await asyncio.start_server(handle_client, IP, PORT)
	print('Сервер запущен.')
	async with server:
		await server.serve_forever()

asyncio.run(main())
