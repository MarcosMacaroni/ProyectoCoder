from django.http import HttpResponse

def Inicio(request):
    return HttpResponse('Bienvenidos a mi Proyecto')