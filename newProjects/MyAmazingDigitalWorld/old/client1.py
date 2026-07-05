#		MADW/client // ☭
# MichiTheCat-RedStar (c) 2026

import asyncio

IP = '127.0.0.1'
PORT = 2077

print('MichiTheCat-RedStar (c) 2026\nДобро пожаловать в MyAmazingDigitalWorld!\n')

async def main():
	reader, writer = await asyncio.open_connection(IP, PORT)
	writer.write(b'Hello')
	await writer.drain()
	answer = await reader.read(1024)

asyncio.run(main())
