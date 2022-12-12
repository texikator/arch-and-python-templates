from utils.templator import render
from views import About, Contacts, Index, CSS
import os



urls = {
    '/': Index(),
    '/about/': About(),
    '/contacts/': Contacts(),
    '/style.css/': CSS()
}

# print(render(template_file))