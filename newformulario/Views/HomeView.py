from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():

    def home(self):
        plantilla = get_template('index.html')
        return HttpResponse(plantilla.render())

    def pagina1(self):

        return HttpResponse('Hoal2')

    def pagina2(self, parametro1):
        return HttpResponse("HOLA DESDE PARAMETRO" + str(parametro1))

    def formulario(self):
        plantilla = get_template('formulario.html')
        return HttpResponse(plantilla.render())
