import mimetypes
import os
import http.server
import socketserver

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

    def _send_text(self, text):
        self.wfile.write(bytes(text, "utf-8"))

    def _not_found(self):
        self.send_response(404)
        self.end_headers()

    def _method_not_allowed(self):
        self.send_response(405)
        self.end_headers()

    def do_request(self, only_headers):
        if str.startswith(self.path, "/static/") and os.path.exists('templates' + self.path):
            self._set_headers(mimetypes.guess_type('templates' + self.path)[0])
        elif str.startswith(self.path, "/player.html"):
            self._set_headers(mimetypes.guess_type('templates/player.html'))
        elif str.startswith(self.path, "/desktop.html"):
            self._set_headers(mimetypes.guess_type('templates/desktop.html'))
        elif str.startswith(self.path, "/"):
            self._set_headers(mimetypes.guess_type('templates/index.html'))
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
