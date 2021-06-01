import json
import mimetypes
import os
import http.server
import socketserver
from config import _CONFIG
from cards import _ALL_PACKS

CACHE = {}
CACHE_ENABLED = False


def get_file_contents(path):
    if CACHE_ENABLED and path in CACHE:
        return CACHE[path]
    with open(path, 'r') as file:
        txt = file.read()
        if CACHE_ENABLED:
            CACHE[path] = txt
        return txt


class SimpleHTTPServer(http.server.BaseHTTPRequestHandler):
    def _set_headers(self, type):
        self.send_response(200)
        self.send_header('Content-type', type)
        self.end_headers()
        self.close_connection = True

    def _set_html_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.close_connection = True

    def _send_text(self, text):
        self.wfile.write(bytes(text, "utf-8"))

    def _not_found(self):
        self.send_response(404)
        self.end_headers()
        self.close_connection = True

    def _method_not_allowed(self):
        self.send_response(405)
        self.end_headers()
        self.close_connection = True

    def do_request(self, only_headers):
        print("do_request(" + str(only_headers) + "), path: " + self.path)
        if str.startswith(self.path, "/static/") and os.path.exists('templates' + self.path):
            self._set_headers(mimetypes.guess_type('templates' + self.path)[0])
        elif str.startswith(self.path, "/static/"):
            self._not_found()
            return
        elif str.startswith(self.path, "/player.html"):
            self._set_html_headers()
        elif str.startswith(self.path, "/desktop.html"):
            self._set_html_headers()
        elif str.endswith(self.path, ".json"):
            self._set_headers("application/json; charset=utf-8")
        elif str.startswith(self.path, "/"):
            self._set_html_headers()
        else:
            self._not_found()
            return
        if not only_headers:
            if str.startswith(self.path, "/static/"):
                self._send_text(get_file_contents('templates' + self.path))
            elif str.startswith(self.path, "/player.html"):
                self._send_text(get_file_contents('templates/player.html'))
            elif str.startswith(self.path, "/desktop.html"):
                self._send_text(get_file_contents('templates/desktop.html'))
            elif self.path == "/config.json":
                self._send_text(json.dumps({
                    "websocket": _CONFIG["host"] + ":" + str(_CONFIG["websocketPort"]),
                    "http": _CONFIG["host"] + ":" + str(_CONFIG["httpPort"])
                }))
            elif self.path == "/sets.json":
                self._send_text(json.dumps(_ALL_PACKS))
            elif str.startswith(self.path, "/"):
                self._send_text(get_file_contents('templates/index.html'))

    def do_GET(self):
        self.do_request(False)

    def do_HEAD(self):
        self.do_request(True)

    def do_POST(self):
        self._method_not_allowed()


def start_webserver(host, port):
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("", port), SimpleHTTPServer) as httpd:
        print("HTTP server started at http://" + host + ":" + str(port) + "/")
        httpd.serve_forever()
