from __future__ import unicode_literals

from sanic.response import json
from sanic.views import HTTPMethodView


class HomepageView(HTTPMethodView):

    async def get(self, request):
        return json({'hello': 'world'})
