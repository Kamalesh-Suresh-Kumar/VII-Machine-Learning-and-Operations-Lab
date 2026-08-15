from http.server import HTTPServer, BaseHTTPRequestHandler

class Handler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = """
        <!DOCTYPE html>
        <html>
        <head>
            <title>Docker Python Web Application</title>
        </head>
        <body>
            <h1>Hello from Docker!</h1>
            <h2>Python Web Application</h2>
            <p>The application is running successfully inside a Docker container.</p>
        </body>
        </html>
        """

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(message.encode())

server = HTTPServer(("0.0.0.0", 8000), Handler)

print("Python web application is running on port 8000...")

server.serve_forever()