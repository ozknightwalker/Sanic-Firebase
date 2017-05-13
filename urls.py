from __future__ import unicode_literals

from sanic import Sanic
from sanic.exceptions import NotFound
from sanic.response import text
from views import *

app = Sanic(__name__)

app.add_route(HomepageView.as_view(), '/')


@app.exception(NotFound)
def ignore_404s(request, exception):
    return text("Yep, I totally found the page: {}".format(request.url))
