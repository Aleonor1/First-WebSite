from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
from requests.compat import quote_plus
from . import models
# Create your views here.

BASE_CRAIGLIST_URL ='https://losangeles.craigslist.org/search/sss?query={}'
BASE_IMAGE_URL = 'https://images.craigslist.org/{}_300x300.jpg'


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

    #image stuff
        if post.find(class_='result-image').get('data-ids'):
            post_image_id = post.find(class_='result-image').get('data-ids').split(',')[0].split(':')[1]
            post_image_url = BASE_IMAGE_URL.format(post_image_id)
            print(post_image_url)
            finalData.append((title, url, price,post_image_url))
        else:
            post_image_url = 'https://craigslist.org/images/peace.jpg'
            finalData.append((title, url, price, post_image_url))

    stuffForFronted={
        'search':search,
        'finalData':finalData,
    }
    return render(request, 'myapp/newSearch.html',stuffForFronted)