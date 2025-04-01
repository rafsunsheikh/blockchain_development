import asyncio

from funcion.blockchain import Blockchain
from funcion.connections import ConnectionPool
from funcion.peers import P2PProtocol
from funcion.server import Server

blockchain = Blockchain()
connection_pool = ConnectionPool()

server = Server(blockchain, connection_pool, P2PProtocol)


async def main():
    # Start the server
    await server.listen()

asyncio.run(main())