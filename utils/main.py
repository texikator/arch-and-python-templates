from pprint import pprint
# from jinja2 import Template
# TEMPLATE_FOLDER = 'templates'

# title = 'welcome!'

class NotFound404():

    def __call__(self, request):
        return "404 WHAT", "Page not Found"

class Framework():

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):

        path = environ['PATH_INFO']
        host = environ.get('HTTP_HOST')
        if not path.endswith('/'):
            path = f'{path}/'
            start_response("301 OK", [("Location", path)])

        request = {}
        request['HTTP_HOST'] = host

        if path in self.urls:
            view = self.urls[path]
        else:
            view = NotFound404()

        code, body = view(request)
        start_response(code, [("Content-type", "text/html")])
        return [body.encode('utf-8')]