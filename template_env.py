from __future__ import unicode_literals

from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import select_autoescape

template_env = Environment(
    loader=PackageLoader('statics', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=True
)
