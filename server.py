#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse

PORT = 5000
HOST = "0.0.0.0"

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        
        # Handle root path
        if path == '/' or path == '/index.html':
            self.path = '/index.html'
        # Handle fonts page
        elif path == '/fonts' or path == '/fonts/':
            self.path = '/fonts.html'
        # Handle assets (CSS, fonts, icons)
        elif path.startswith('/assets/'):
            self.path = path
        # Handle public fonts
        elif path.startswith('/public/'):
            self.path = path
        # Handle metagraph image
        elif path == '/metagraph-img.jpg':
            self.path = '/metagraph-img.jpg'
        # Handle other files
        else:
            if os.path.exists('.' + path) and os.path.isfile('.' + path):
                self.path = path
            else:
                self.path = '/404.html'
        
        return super().do_GET()

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer((HOST, PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Server running at http://{HOST}:{PORT}/")
        print(f"Serving static files from: {os.getcwd()}")
        httpd.serve_forever()
