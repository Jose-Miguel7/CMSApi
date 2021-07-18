from django.shortcuts import render

from django.views.generic import TemplateView

from .models import Endpoint, Parametro

class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        seccion = self.request.path.split('/')[-2].capitalize()
        context['titulo_seccion'] = seccion

        endpoints = Endpoint.objects.filter(seccion=seccion)
        content = []
        for endpoint in endpoints:
            parametros = Parametro.objects.filter(endpoint=endpoint)
            query = True if parametros.exists() else False
            obj = {
                "endpoint": endpoint,
                "parameters": parametros,
                "query": query
            }
            content.append(obj)

        context['contenido'] = content
        return context

class Home(TemplateView):
    template_name = 'home.html'