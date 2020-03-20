from django.shortcuts import render

# Create your views here.


def homeView(request):
    return render(request,  'base.html')

def newSearch(request):
    search = request.POST.get('search')
    stuffForFronted={
        'search':search
    }
    return render(request, 'myapp/newSearch.html',stuffForFronted)