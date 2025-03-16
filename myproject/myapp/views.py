from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello World")
def homepage(request):
    return HttpResponse("Welcome to Little Lemon")
import datetime

def display_date(request):
    date_joined = datetime.datetime.now().year
    return HttpResponse(f"Year: {date_joined}")
def menu(request):
    html_content = """
    <html>
        <head><title>Little Lemon Menu</title></head>
        <body style="background-color: #f4f4f4;">
            <h1 style="color: #4CAF50;">Little Lemon Menu</h1>
            <ul>
                <li>Pizza - $10</li>
                <li>Pasta - $12</li>
                <li>Burger - $8</li>
            </ul>
        </body>
    </html>
    """
    return HttpResponse(html_content)

from django.http import HttpResponse

def home(request):
    path = request.path  
    return HttpResponse(path, content_type="text/plain", charset="utf-8")
