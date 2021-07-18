from django.db import models

class Section(models.Model):
    nombre = models.CharField('Sección', max_length=20, primary_key=True)

    def __str__(self):
        return self.nombre

class Endpoint(models.Model):
    metodo = models.CharField('Método', max_length=10)
    titulo_metodo = models.CharField('Título Método', max_length=50, unique=True)
    request_example = models.TextField('Request Example')
    descripcion = models.TextField('Descripción')
    url = models.URLField('Url')
    response_example = models.TextField('Response Example')
    seccion = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo_metodo

class Parametro(models.Model):
    endpoint = models.ForeignKey(Endpoint, on_delete=models.CASCADE)
    field = models.CharField('Field', max_length=50)
    tipo = models.CharField('Tipo', max_length=50)
    descripcion = models.TextField('Descripción')

    def __str__(self):
        return str(self.endpoint) + ' - ' + self.field
