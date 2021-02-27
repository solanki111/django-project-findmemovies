from django.shortcuts import render
from .functions import TheMovieDb
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


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
    return render(request, 'search_engine/card_view.html', context)


def check_response(response):
    if response.status_code == 200:
        return response.json()
    elif response.status_code == 404:
        return render('404.html')
    elif response.status_code == 403:
        return render('403.html')
    elif response.status_code == 500:
        return render('500.html')
    else:
        return render('400.html')
