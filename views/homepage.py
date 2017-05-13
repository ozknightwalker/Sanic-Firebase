from __future__ import unicode_literals

from core.views import TemplateView


class HomepageView(TemplateView):
    template_name = 'base.html'

    def get_method(self, request):
        context = {'title': 'Sanic'}
        return context
