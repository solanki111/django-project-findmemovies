from django.shortcuts import render, redirect
from pprint import pprint as pp
from .functions import TheMovieDb
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.views.defaults import page_not_found, server_error, permission_denied


@csrf_exempt
@cache_page(1000)
@require_http_methods(['GET'])
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        return render(request, '403.html')


def search(request):
    if request.method == 'GET':
        return render(request, 'search_engine/movie_search.html')
    elif request.method == 'POST':
        query = request.POST.get('q')
        if all(x.isalpha() or x.isspace() for x in query) and query is not None:
            movie_db = TheMovieDb()
            response = movie_db.api_request('ser', f'&query={query}')
            results = check_response(response)
            if results.get('results'):
                return render(request, 'search_engine/card_view.html', results)
            else:
                return render(request, '404.html')
        else:
            return render(request, '404.html')


def similar_movie(request, movie_id):
    pp(f'sim-movie_id>>>> {movie_id}')
    if movie_id is not None:
        movie_db = TheMovieDb()
        response = movie_db.api_request('sim', movie_id)
        results = check_response(response)
        if results.get('results'):
            return render(request, 'search_engine/card_view.html', results)
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')


def similar_tv(request, tv_id):
    pp(f'sim-tv_id>>>> {tv_id}')
    if tv_id is not None:
        movie_db = TheMovieDb()
        response = movie_db.api_request('sit', tv_id)
        results = check_response(response)
        if results.get('results'):
            return render(request, 'search_engine/card_view.html', results)
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')


def movie(request, movie_id):
    pp(f'movie_id>>>> {movie_id}')
    if movie_id is not None:
        movie_db = TheMovieDb()
        response = movie_db.api_request('mov', movie_id)
        results = check_response(response)
        if results:
            context = {
                'results': results
            }
            return render(request, 'search_engine/full_view.html', context)
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')


def tv(request, tv_id):
    pp(f'tv_id>>>> {tv_id}')
    pp(tv_id)
    if tv_id is not None:
        movie_db = TheMovieDb()
        response = movie_db.api_request('tv', tv_id)
        results = check_response(response)
        if results:
            context = {
                'results': results
            }
            return render(request, 'search_engine/full_view.html', context)
        else:
            return render(request, '404.html')
    else:
        return render(request, '404.html')


def popular(request):
    movie_db = TheMovieDb()
    response = movie_db.api_request('pop')
    results = check_response(response)
    if results.get('results'):
        return render(request, 'search_engine/card_view.html', results)
    else:
        return render(request, '404.html')


def trending(request):
    movie_db = TheMovieDb()
    response = movie_db.api_request('tre')
    results = check_response(response)
    if results.get('results'):
        return render(request, 'search_engine/card_view.html', results)
    else:
        return render(request, '404.html')


def discover(request):
    context = {
        'object': {}
    }
    return render(request, 'search_engine/discover.html', context)


def check_response(response):
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        raise page_not_found
    elif response.status_code == 403:
        raise permission_denied
    elif response.status_code == 500:
        raise server_error
    else:
        return render('400.html')