from __future__ import unicode_literals

import os

from sanic import Sanic
from sanic.response import json

app = Sanic()


@app.route("/")
async def homepage(request):
    return json({'hello': 'world'})

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
