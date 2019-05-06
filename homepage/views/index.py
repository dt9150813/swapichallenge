from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
import requests
import json
from django.http import JsonResponse

@view_function
def process_request(request):
    if 'films' not in request.session:
        print('Getting films')
        url = "https://swapi.co/api/films"
        response = requests.request("GET", url)
        result = response.json()
        films = [[0 for x in range(8)] for y in range(7)]
        for i in range (7):
            films[i][0] = str(result['results'][i]['title'])
            films[i][1] = int(result['results'][i]['episode_id'])
            films[i][2] = str(result['results'][i]['release_date'])
            #Getting the correct sequence number for SWAPI
            if films[i][1] <= 3:
                films[i][3] = films[i][1] + 3
            elif 4 <= films[i][1] <= 6:
                films[i][3] = films[i][1] - 3
            else:
                films[i][3] = films[i][1]
            films[i][4] = str(result['results'][i]['opening_crawl'])
            films[i][5] = str(result['results'][i]['director'])
            films[i][6] = str(result['results'][i]['producer'])
            url1 = "http://www.omdbapi.com/"
            querystring1 = {"apikey":"66e22f97","s":films[i][0],"y":films[i][2][:4]}
            response1 = requests.request("GET", url1, params=querystring1)
            result1 = response1.json()
            films[i][7] = str(result1['Search'][0]['Poster']).replace("._V1_SX300", "")
        request.session['films'] = films
        context = {
            'films': request.session['films'],
        }
        return request.dmp.render('index.html', context)
    else:
        context = {
            'films': request.session['films'],
        }
        return request.dmp.render('index.html', context)
