import asyncio
import mimetypes
import os
import threading
import websockets
import http.server
import socketserver

HTTP_PORT = 80
WEBSOCKET_PORT = 8080
CACHE = []


async def hello(websocket, path):
    name = await websocket.recv()
    print(f"< {name}")
    greeting = f"Hello {name}!"
    await websocket.send(greeting)
    print(f"> {greeting}")


class SimpleHTTPServer(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, type):
        self.send_response(200)
        self.send_header('Content-type', type)
        self.end_headers()

    def _send_text(self, text):
        self.wfile.write(bytes(text, "utf-8"))

    def _not_found(self):
        self.send_response(404)
        self.end_headers()

    def _method_not_allowed(self):
        self.send_response(405)
        self.end_headers()

    def do_request(self, only_headers):
        if str.startswith(self.path, "/static/") and os.path.isfile('templates' + self.path):
            self._set_headers(mimetypes.guess_type('templates' + self.path)[0])
        elif str.startswith(self.path, "/"):
            self._set_headers(mimetypes.guess_type('templates/index.html'))
        elif str.startswith(self.path, "/player.html"):
            self._set_headers(mimetypes.guess_type('templates/player.html'))
        elif str.startswith(self.path, "/desktop.html"):
            self._set_headers(mimetypes.guess_type('templates/desktop.html'))
        else:
            self._not_found()
            return
        if not only_headers:
            if str.startswith(self.path, "/static/"):
                with open('templates' + self.path, 'r') as file:
                    self._send_text(file.read())
            elif str.startswith(self.path, "/"):
                with open('templates/index.html', 'r') as file:
                    self._send_text(file.read())
            elif str.startswith(self.path, "/player.html"):
                with open('templates/player.html', 'r') as file:
                    self._send_text(file.read())
            elif str.startswith(self.path, "/desktop.html"):
                with open('templates/desktop.html', 'r') as file:
                    self._send_text(file.read())

    def do_GET(self):
        self.do_request(False)

    def do_HEAD(self):
        self.do_request(True)

    def do_POST(self):
        self._method_not_allowed()


def start_webserver():
    with socketserver.TCPServer(("", HTTP_PORT), SimpleHTTPServer) as httpd:
        print("serving at port", HTTP_PORT)
        httpd.serve_forever()


def start_websocket():
    asyncio.set_event_loop(asyncio.new_event_loop())
    start_server = websockets.serve(hello, 'localhost', WEBSOCKET_PORT)
    print("serving at port", WEBSOCKET_PORT)
    asyncio.get_event_loop().run_until_complete(start_server)


def start_everything():
    threading.Thread(target=start_webserver).start()
    threading.Thread(target=start_websocket).start()


if __name__ == '__main__':
    start_everything()
