import urllib.request
import urllib.parse
import json

def load_json_data_from_url(base_url, url_params):
    try:
        url = '%s?%s' % (base_url, urllib.parse.urlencode(url_params))
        response = urllib.request.urlopen(url).read().decode('utf-8')
        load_data = json.loads(response)
    except urllib.error.HTTPError:
        load_data = "No info"
    return load_data


def get_movie_details(method, api_key, extra_params=None):
    extra_params = extra_params or {}
    url = 'https://api.themoviedb.org/3%s' % method
    params = {
        'api_key': api_key,
        'language': 'ru',
    }
    params.update(extra_params)
    return load_json_data_from_url(url, params)


def get_movie_recommendations(method, api_key):
    url = 'https://api.themoviedb.org/3%s' % method + '/recommendations?api_key=' + api_key
    try:
        response = urllib.request.urlopen(url).read().decode('utf-8')
        load_data = json.loads(response)
    except urllib.error.HTTPError:
        load_data = "No recommendations"
    return load_data

db = {}
for i in range(11000, 12000):
    db[i] = [get_movie_details(method='/movie/' + str(i), api_key='44db884e65e6442979b115815c9ba203')] #Качаю основную инфу о фильмах
    if db[i] != ["No info"]:
        # Качаю все рекомендции к фильмам (эту информацию нигде потом не использую)
        db[i].append(get_movie_recommendations(method='/movie/' + str(i), api_key='44db884e65e6442979b115815c9ba203'))
# Записываю в json файл
write_info = open('mydb.json', 'w')
write_info.write(json.dumps(db))
write_info.close()
