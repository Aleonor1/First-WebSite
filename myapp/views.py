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

    postListings = soup.find_all('li', {'class': 'result-row'})

    finalData = []

    for post in postListings:
        title = post.find(class_='result-title').text
        url = post.find('a').get('href')
        price = post.find(class_='result-price').text if post.find(class_='result-price') else 'N/A'
        finalData.append((title,url,price))

    stuffForFronted={
        'search':search,
        'finalData':finalData,
    }
    return render(request, 'myapp/newSearch.html',stuffForFronted)