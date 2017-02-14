import json

def get_movie_param(json_data,movie_id):
    params = {}
    if 'genres' in json_data[movie_id][0].keys():
        # получаю информацию о всех жанрах фильма
        genres_info = []
        for i in range(len(json_data[movie_id][0]['genres'])):
            genres_info.append(json_data[movie_id][0]['genres'][i]['name'])
        params['genres'] = genres_info
    else:
        pass
    if 'belongs_to_collection' in json_data[movie_id][0].keys() and json_data[movie_id][0]['belongs_to_collection'] is not None:
        # получаю информацию о отнощение к какой нибудь серии фильмов
        belongs_to_collection = str(json_data[movie_id][0]['belongs_to_collection']['name'])
        params['collection'] = belongs_to_collection
    else:
        pass
    if 'release_date' in json_data[movie_id][0].keys():
        # получаю информацию о годе выпуска
        release_date = str(json_data[movie_id][0]['release_date'])
        params['year'] = release_date[:4]
    else:
        pass
    return params

def get_movie_recom(json_data,params):
    # У каждого фильма есть свои баллы рекомендации
    recom_points = {}
    for movie_id in json_data:
        posib_recom = {}
        if json_data[movie_id][0] != 'No info':
            if 'title' in json_data[movie_id][0].keys():
                # Записываю название фильма(для рекомендации) в ключ, а значение - кол-во баллов рекомендации (изначально 0)
                title = (str(json_data[movie_id][0]['title'])).lower()
                recom_points[title] = 0
                if 'genres' in json_data[movie_id][0].keys():
                    # Собираю инфу о жанре фильма для рекомендации
                    genres_info = []
                    for i in range(len(json_data[movie_id][0]['genres'])):
                        genres_info.append(json_data[movie_id][0]['genres'][i]['name'])
                    posib_recom['genres'] = genres_info
                else:
                    pass
                if 'belongs_to_collection' in json_data[movie_id][0].keys() and json_data[movie_id][0]['belongs_to_collection'] is not None:
                    # Собираю инфу о серии фильма для рекомендации
                    belongs_to_collection = str(json_data[movie_id][0]['belongs_to_collection']['name'])
                    posib_recom['collection'] = belongs_to_collection
                else:
                    pass
                if 'release_date' in json_data[movie_id][0].keys():
                    # Собираю инфу о годе выпуска фильма для рекомендации
                    release_date = str(json_data[movie_id][0]['release_date'])
                    posib_recom['year'] = release_date[:4]
                else:
                    pass
                if ('genres' in params) and ('genres' in posib_recom):
                    # Сверяю жанры и даю баллы(2) за каждый схожий жанр
                    for my_genres in params['genres']:
                        for pos_genres in posib_recom['genres']:
                            if my_genres == pos_genres:
                                recom_points[title] += 2
                else:
                    pass
                if ('collection' in params) and ('collection' in posib_recom):
                    # Сверяю серии и даю балла(3) за схожие серии
                    if params['collection'] == posib_recom['collection']:
                        recom_points[title] += 3
                else:
                    pass
                if ('genres' in params) and ('year' in posib_recom):
                    # Сверяю года выпуска и даю баллы(1) за одинаковые года
                    if params['year'] == posib_recom['year']:
                        recom_points[title] += 1
                else :
                    pass
            else:
                pass
    return recom_points


print('Введите название фильма:')  # Примеры: Клетка для пташек, Жанна Д'Арк, Полицейская академия 6: Город в осаде
search_movie = (str(input())).lower()
d = open('mydb.json','r')
json_data = json.load(d)
d.close()
for movie_id in json_data:
    if json_data[str(movie_id)] != ['No info']:  # т.к. не у всех id есть инфа, то проверяю, чтобы была
        if search_movie == json_data[movie_id][0]['title'].lower():
            # Если нахожу название такого фильма, то получаю всю нужную информацию для рекомендаций
            movie_params = get_movie_param(json_data,movie_id)
if 'movie_params' in globals():
    # Получаю информацию о остальных фильмах в бд и их соотношении с выбранным фильмом
    movie_points = get_movie_recom(json_data,movie_params)
    movie_points.pop(search_movie)
    for name,points in movie_points.items():
        if points >= 5:
            print('Вам точно понравится:',name.title())
        elif 3 <= points <= 4:
            print('Скорее всего вам понравится:', name.title())
        elif points == 2:
            print('Возможно вам понравится:',name.title())
else:
    print('Такого фильма нет!')
