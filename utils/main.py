from pprint import pprint
from .requests import GetRequest, PostRequest
# from jinja2 import Template
# TEMPLATE_FOLDER = 'templates'

# title = 'welcome!'


class NotFound404:

    def __call__(self, request):
        return "404 WHAT", "Page not Found"


class Framework:

    def __init__(self, urls):
        self.urls = urls

    def __call__(self, environ, start_response):
        request = {}
        # pprint(environ)
        path = environ['PATH_INFO']

        if path.endswith(".css/"):
            content_type = "text/css"
        else:
            content_type = "text/html"

        if not path.endswith('/'):
            path = f'{path}/'
            print('Дописали /')
            start_response("302 Found", [("Location", path)])
            return [b'redirect']

        host = environ.get('HTTP_HOST')
        request['HTTP_HOST'] = host

        request_method = environ.get('REQUEST_METHOD')
        request['REQUEST_METHOD'] = request_method

        if request_method == 'GET':
            request_data = GetRequest().get_request_data(environ)
            print(f'GET запрос, данные: {request_data}')
            request['query_params'] = request_data
        elif request_method == 'POST':
            request_data = PostRequest().get_request_data(environ)
            print(f'POST запрос, данные: {request_data}')
            request['data'] = request_data

        view = self.urls[path] if path in self.urls else NotFound404()

        code, body = view(request)
        start_response(code, [("Content-type", content_type)])
        return [body.encode('utf-8')]

