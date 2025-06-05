from django.http import HttpResponse

def home_page(request):
    print("Home page")
    
    return HttpResponse("<h1>This is home page<h1>")