from __future__ import unicode_literals

from sanic.response import html
from sanic.views import HTTPMethodView

from template_env import template_env


class View(HTTPMethodView):

    def get_method(self, request):
        return {}

    def get_template(self):
        return template_env.get_template(self.template_name)


class TemplateView(View):
    template_name = ''

    async def get(self, request):
        context = self.get_method(request)
        template = self.get_template()
        return html(template.render(context))

    def get_method(self, request):
        return {}
