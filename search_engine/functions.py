import requests
from pprint import pprint as pp
import os


class RapidApi:

    def __init__(self):
        pass

    def header(self):
        return {
            'x-rapidapi-host': os.environ.get('rapid_host'),
            'x-rapidapi-key': os.environ.get('rapid_key')
        }

    def url(self):
        return os.environ.get('rapid_url')

    def api_options(self, api_option):
        api_req = {
            'auto': 'auto-complete',
            'metadata': 'get-meta-data',
            'morelikethis': 'get-more-like-this',
            'moviesbygenre': 'get-popular-movies-by-genre'
        }
        req = api_req.get(api_option)
        return req

    def api_request(self, querystring, api_option):
        full_url = self.url() + self.api_options(api_option)
        pp(full_url)
        response = requests.request("GET", full_url, headers=self.header(), params=querystring)
        pp(response)
        return response.json()


class TheMovieDb:

    def __init__(self):
        pass

    def api_key(self):
        return os.environ.get('moviedb_key')

    def url(self):
        return os.environ.get('moviedb_url')

    def api_options(self, api_option):
        api_req = {
            'dis': 'discover/movie',
            'ser': 'search/movie',
            'mov': 'movie/',
            'tv': 'tv/',
            'sim': '/similar',
            'sit': '/similar',
            'pop': 'movie/popular',
            'tre': 'trending/all/day'
        }
        req = api_req.get(api_option)
        return req

    def api_request(self, *options):
        full_url = None
        if options[0] == "dis":
            full_url = self.url() + self.api_options(options[0]) + self.api_key() + 'rest_url' + os.environ.get('moviedb_rest_url')
        elif options[0] == "ser":
            full_url = self.url() + self.api_options(options[0]) + self.api_key() + options[1] + os.environ.get('moviedb_rest_url')
        elif options[0] == "mov":
            full_url = self.url() + self.api_options(options[0]) + options[1] + self.api_key() + os.environ.get('moviedb_rest_url')
        elif options[0] == "sim":
            full_url = self.url() + self.api_options('mov') + options[1] + self.api_options(options[0]) + self.api_key() + os.environ.get('moviedb_rest_url')
        elif options[0] == "sit":
            full_url = self.url() + self.api_options('tv') + options[1] + self.api_options(options[0]) + self.api_key() + os.environ.get('moviedb_rest_url')
        elif options[0] == "pop":
            full_url = self.url() + self.api_options(options[0]) + self.api_key() + os.environ.get('moviedb_rest_url')
        elif options[0] == "tre":
            full_url = self.url() + self.api_options(options[0]) + self.api_key()
        elif options[0] == "tv":
            full_url = self.url() + self.api_options(options[0]) + options[1] + self.api_key() + os.environ.get('moviedb_rest_url')

        response = requests.request("GET", full_url)
        return response
