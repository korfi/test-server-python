import http.server
import socketserver

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = 'index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

port = 8000
address = ("", port)

handler = MyHttpRequestHandler

httpd = socketserver.TCPServer(address, handler)
print("Serwer działa na porcie " + str(port))
httpd.serve_forever()
