#!/usr/bin/env python3
import http.server
import socketserver
import os
from urllib.parse import urlparse

class CustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add no-cache headers to prevent caching issues in Replit
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # Parse the requested path
        parsed_path = urlparse(self.path)
        file_path = parsed_path.path.lstrip('/')
        
        # Route handling
        if not file_path or file_path == '/':
            file_path = 'index.html'
        elif file_path == 'fonts' or file_path == 'fonts/':
            file_path = 'fonts.html'
        
        # Check if the requested file exists
        if os.path.exists(file_path) and os.path.isfile(file_path):
            # File exists, serve it normally
            super().do_GET()
        else:
            # File doesn't exist, serve 404.html with 404 status
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            try:
                with open('404.html', 'rb') as f:
                    self.wfile.write(f.read())
            except FileNotFoundError:
                # Fallback if 404.html doesn't exist
                self.wfile.write(b'<html><body><h1>404 - Page Not Found</h1></body></html>')

if __name__ == "__main__":
    PORT = 5000
    # Allow reuse of address to prevent "Address already in use" errors
    socketserver.TCPServer.allow_reuse_address = True
    with socketserver.TCPServer(("0.0.0.0", PORT), CustomHTTPRequestHandler) as httpd:
        print(f"Serving HTTP on 0.0.0.0 port {PORT} (http://0.0.0.0:{PORT}/) ...")
        httpd.serve_forever()