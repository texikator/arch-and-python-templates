from wsgiref.simple_server import make_server
from utils.main import Framework
from urls import urls

PORT = 8080
app = Framework(urls)

with make_server('', PORT, app) as httpd:
    print(f"Server at {PORT} listen ....  ")
    httpd.serve_forever()
    # httpd.handle_request()
