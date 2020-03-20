from django.shortcuts import render

# Create your views here.


def homeView(request):
    return render(request,  'base.html')

def newSearch(request):
    return render(request, 'myapp/newSearch.html')