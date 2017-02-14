import json

def movie_info(movie_id):
    if json_data[movie_id] != ['No info']:
        if 'title' in json_data[movie_id][0].keys():
            # Записываю всю инфу о названии фильма
            title = str(json_data[movie_id][0]['title'])
            if 'genre' in json_data[movie_id][0].keys():
                # Записываю всю инфу о жанрах
                genres_info = str()
                for i in range(len(json_data[movie_id][0]['genres'])):
                    genres_info += str(json_data[movie_id][0]['genres'][i]['name'])
            else:
                genres_info = ''
            if 'production_companies' in json_data[movie_id][0].keys():
                # Записываю всю инфу о компаниях
                companies_info = str()
                for i in range(len(json_data[movie_id][0]['production_companies'])):
                    companies_info += str(json_data[movie_id][0]['production_companies'][i]['name'])
            else:
                companies_info = ''
            if 'release_date' in json_data[movie_id][0].keys():
                # Записываю всю инфу о дате выхода
                release_date = str(json_data[movie_id][0]['release_date'])
            else:
                release_date = ''
            if 'overview' in json_data[movie_id][0].keys():
                # Записываю всю инфу о описании
                overview = str(json_data[movie_id][0]['overview'])
            else:
                overview = ''
            if 'belongs_to_collection' in json_data[movie_id][0].keys() and json_data[movie_id][0]['belongs_to_collection'] is not None:
                # Записываю всю инфу о серии фильма
                belongs_to_collection = str(json_data[movie_id][0]['belongs_to_collection']['name'])
            else:
                belongs_to_collection = ''
            if 'original_title' in json_data[movie_id][0].keys():
                # Записываю всю инфу о оригинальном названии
                original_title = str(json_data[movie_id][0]['original_title'])
            else:
                original_title = ''
            # Всю эту инфу записываю в одну переменную и возращаю
            full_info = (title + ' ' + release_date + ' ' + genres_info + ' ' + overview + ' ' + belongs_to_collection + ' ' + companies_info + ' ' + original_title).lower()
        else: full_info = ''
    else: full_info = ''
    return full_info

print('Введите слово:')
search_param = (str(input())).lower()
db = open('mydb.json', 'r')
json_data = json.load(db)
db.close()
found = False
for movie_id in json_data:
    if search_param in (movie_info(movie_id)): #Я ищу слово во всех источниках(названии,жанрах,команиях(которые продюсировали),дате выхода, описании, в оригинальном названии и серии фильмов
        print(json_data[movie_id][0]['title'],json_data[movie_id][0]['release_date'])
        found = True
if not found:
    print('Ничего не нашлось :(')