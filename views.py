from utils.templator import render
from os.path import join
from os import environ
TEMPLATE_DIR = 'templates'
TEMPLATE_NAME = 'textured_green'
TEMPLATE_FILE = 'index.html'
CSS_FILE = 'style.css'
template = join(TEMPLATE_DIR, TEMPLATE_NAME, TEMPLATE_FILE)
css = join(TEMPLATE_DIR, TEMPLATE_NAME, CSS_FILE)


class Index:

    def __call__(self, request):
        data = {}
        data['title'] = 'title'
        data['content'] = 'Это контент'
        data['HTTP_HOST'] = request.get('HTTP_HOST')

        return "200 OK", render(template, data=data)

class About:
    def __call__(self, request):
        data = {}
        data['title'] = "О Компании"
        data['content'] = "Компания Рога и Копыта - лидер на рынке .... "
        data['HTTP_HOST'] = request.get('HTTP_HOST')

        return "200 OK", render(template, data=data)

class Contacts:
    def __call__(self, request):
        data = {}
        data['title'] = "Наши контакты"
        data['content'] = "Мы расположены там то и сям то ... "
        return "200 OK", render(template, data=data)


class CSS:
    def __call__(self, request):
        return "200 OK", render(css)


if __name__ == "__main__":
    a = Base()
    print(a.menu_items)
