from jinja2 import Template
from jinja2.loaders import FileSystemLoader

def render(template_name, **kwargs):
    with open(template_name, encoding='utf-8') as f_n:
        template = Template(f_n.read())

    return template.render(**kwargs)

