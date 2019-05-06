from django.conf import settings
from django_mako_plus import view_function, jscontext
from datetime import datetime, timezone
import requests
import json
from django.http import JsonResponse
from django.shortcuts import redirect


@view_function
def process_request(request, sequence):
    #Check if the user already got their films from SWAPI
    if 'films' not in request.session:
        return redirect('/homepage/index/')

    else:
        for i in range(len(request.session['films'])):
            if request.session['films'][i][3] == int(sequence):
                index = i
        title = request.session['films'][index][0]
        episode_id = request.session['films'][index][1]
        release_date = request.session['films'][index][2]
        sequence_id = request.session['films'][index][3]
        opening_crawl = request.session['films'][index][4]
        director = request.session['films'][index][5]
        producer = request.session['films'][index][6]
        img = request.session['films'][index][7]

        context = {
            'title': title,
            'episode_id': episode_id,
            'opening_crawl': opening_crawl,
            'director': director,
            'producer': producer,
            'release_date': release_date,
            'sequence_id': sequence_id,
            'img': img,
        }
        return request.dmp.render('film.html', context)

