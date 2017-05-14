from __future__ import unicode_literals

from sanic.response import html
from sanic.views import HTTPMethodView
from sanic.exceptions import NotFound

from template_env import template_env


class View(HTTPMethodView):
    methods = []

    def get_method(self, request):
        return {}

    def get_template(self):
        return template_env.get_template(self.template_name)

    def get_context_data(self, request):
        return {}

    def get_meta_data(self):
        pass

    def dispatch(self, request):
        if request.method.lower() not in self.methods:
            raise NotFound("Method Not Allowed", status_code=405)


class TemplateView(View):
    template_name = ''
    methods = ['get']

    async def get(self, request):
        self.dispatch(request)
        context = self.get_context_data(request)
        template = self.get_template()
        return html(template.render(context))

    def get_method(self, request):
        return {}
