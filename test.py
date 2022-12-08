from pprint import pprint
def app(environ, start_response):
    pprint(environ)
    data = b"Hello world"
    start_response("200 OK", [("Content-Type", "text/plain")])

    return [data]