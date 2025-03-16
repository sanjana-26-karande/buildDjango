from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, Welcome to Little Lemon!")

def menu(request):
    return HttpResponse("This is the menu page.")