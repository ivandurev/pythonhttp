import os
from http.server import BaseHTTPRequestHandler
import urllib, json
from routes.main import routes
from routes.main import api_routes
from response.staticHandler import StaticHandler
from response.badRequestHandler import BadRequestHandler
from response.apiHandler import ApiHandler

class Server(BaseHTTPRequestHandler):
    def do_HEAD(self):
        return
    def do_POST(self):
        handler = ApiHandler()
        content_length = int(self.headers['Content-Length'])
        content_str = self.rfile.read(int(self.headers['Content-Length']))
        
        content = urllib.parse.parse_qs(content_str)
        #print(urllib.parse.parse_qs(self.path[2:]))
        if self.path in api_routes:
            handler.execute(api_routes[self.path], content)
            handler.contents.write(urllib.parse.quote(handler.getContents()))
        else:
            handler = BadRequestHandler()

        self.respond({
            'handler' : handler
        })

    def do_GET(self):

        handler = StaticHandler()
        alt = routes['static']['path']+self.path

        if self.path in routes:

            file_found = handler.find(routes[self.path])
            if file_found == 0:
                handler = BadRequestHandler()
        elif os.path.isfile(alt):
            temp_route = {'path' : alt}
            file_found = handler.find(temp_route)
            if file_found == 0:
                handler = BadRequestHandler()
        else:
            handler = BadRequestHandler()
        self.respond({
            'handler': handler
        })

      
    def handle_http(self, handler):
        status_code =  handler.getStatus()
        self.send_response(status_code)

        content = handler.getContents()
        self.send_header('Content-type', handler.getContentType())
        self.end_headers()
        if isinstance( content, (bytes, bytearray) ):
            return content

        return bytes(content, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['handler'])
        self.wfile.write(response)