from __future__ import unicode_literals

import os

from sanic import Sanic

app = Sanic(__name__)

from urls import *

app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 8000)))
