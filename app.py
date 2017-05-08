from __future__ import unicode_literals

import os

from sanic import Sanic

from jinja2 import Environment, PackageLoader, select_autoescape

app = Sanic(__name__)

template_env = Environment(
    loader=PackageLoader('jinja_example', 'templates'),
    autoescape=select_autoescape(['html', 'xml']),
    enable_async=True
)

from urls import *

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
