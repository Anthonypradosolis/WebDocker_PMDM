import http.server
import socketserver
from http import HTTPStatus
from logging import Handler


class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header()
        self.wfile.write(b'Hello, world')



def print_hi(name):
    print(f'Hi, {name}')



if __name__ == '__main__':
    print_hi('PyCon')
    httpd=socketserver.TCPServer(("", 8000), Handler)
    httpd.serve_forever()