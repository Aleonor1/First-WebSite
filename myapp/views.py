from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models
# Create your views here.

BASE_CRAIGLIST_URL ='https://losangeles.craigslist.org/search/sss?query={}'

def homeView(request):
    return render(request,  'base.html')

def newSearch(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_CRAIGLIST_URL.format(quote_plus(search))
    response = requests.get(final_url)
    data = response.text
    soup = BeautifulSoup(data, features='html.parser')
    soup_title = soup.find_all('a',{'class': 'result-title'})
    print(soup)
    stuffForFronted={
        'search':search
    }
    return render(request, 'myapp/newSearch.html',stuffForFronted)