from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Endpoint, Parametro, Section


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, section, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        seccion = section.capitalize()
        context['titulo_seccion'] = seccion
        print(seccion)

        sections = Section.objects.all()
        endpoints = Endpoint.objects.filter(seccion=section)
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
        context['sections'] = sections
        return context


class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(Home, self).get_context_data(**kwargs)
        sections = Section.objects.all()
        context['sections'] = sections
        return context
