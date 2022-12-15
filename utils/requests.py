from quopri import decodestring

class BaseRequest:

    @staticmethod
    def decode_value(raw_string):
        raw_string = bytes(raw_string.replace("%", "=").replace("+", " "), 'UTF-8')
        result = decodestring(raw_string).decode('UTF-8')
        return result

    @staticmethod
    def parse_query_string(query_string):
        params = query_string.split('&')
        print(f'params: {params}')
        result = {k: BaseRequest.decode_value(v) for k, v in [param.split("=") for param in params]}
        return result


class GetRequest(BaseRequest):

    def get_request_data(self, environ):
        # result = {}
        raw_data = environ.get('QUERY_STRING')
        result = self.parse_query_string(raw_data) if raw_data else {}

        return result


class PostRequest(BaseRequest):

    @staticmethod
    def get_wsgi_data(env):
        raw_wsgi_data = env.get('wsgi.input')
        data_length_raw = env.get('CONTENT_LENGTH')
        data_length = int(data_length_raw) if data_length_raw else 0
        result = raw_wsgi_data.read(data_length) if data_length > 0 else b''
        return result

    def parse_wsgi_data(self, raw_data):
        result = {}
        if raw_data:
            data = raw_data.decode(encoding='utf-8')
            result = self.parse_query_string(data)

        print(f'Данные POST в виде строки {result}')
        return result

    def get_request_data(self, environ):
        data = self.get_wsgi_data(environ)
        result = self.parse_wsgi_data(data)
        return result
