import asyncio
import json

import websockets


async def handle_undefined_packet(websocket, packet):
    print("undefined command", packet["command"])


class WebsocketServer:
    def __init__(self, open_handler, close_handler, packet_handlers):
        self.packet_handlers = packet_handlers
        self.close_handler = close_handler
        self.open_handler = open_handler

    async def websocket_handler(self, websocket, path):
        print("Client connection at " + websocket.remote_address[0])
        await self.open_handler(websocket)
        try:
            while True:
                data = await websocket.recv()
                packet = json.loads(data)
                handler = self.packet_handlers.get(packet["command"], handle_undefined_packet)
                await handler(websocket, packet)
        except websockets.ConnectionClosed:
            print("Connection closed at " + websocket.remote_address[0])
            await self.close_handler(websocket)


def start_websocket(host, port, open_handler, close_handler, packet_handlers):
    wserver = WebsocketServer(open_handler, close_handler, packet_handlers)
    asyncio.set_event_loop(asyncio.new_event_loop())
    start_server = websockets.serve(wserver.websocket_handler, host, port)
    asyncio.get_event_loop().run_until_complete(start_server)
    print("Websocket started at ws://" + host + ":" + str(port) + "/")
    asyncio.get_event_loop().run_forever()
