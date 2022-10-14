from http.server import HTTPServer, SimpleHTTPRequestHandler

httpd = HTTPServer(('0.0.0.0', 8081), SimpleHTTPRequestHandler)
httpd.serve_forever()
