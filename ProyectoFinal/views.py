from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola, esta es una view de prueba")
    