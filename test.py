import pydantic_models
import app
fake_database = {'users':[
    {
        "id":1,             # тут тип данных - число
        "name":"Anna",      # тут строка
        "nick":"Anny42",    # и тут
        "balance": 15300    # а тут float
     },
    {
        "id":2,             # у второго пользователя
        "name":"Dima",      # такие же
        "nick":"dimon2319", # типы
        "balance": 160.23     # данных
     }
    ,{
        "id":3,             # у третьего
        "name":"Vladimir",  # юзера
        "nick":"Vova777",   # мы специально сделаем
        "balance": "25000"     # нестандартный тип данных в его балансе
     }
],}
id = 2
user = {
    "id":4,
    "name": "debil",
    "nick": "her",
    "balance": 13.4
}

for index, u in enumerate(fake_database['users']):
    if u['id'] == id:
        fake_database['users'][index] = user
print(fake_database['users'])

a = app.query('j')
print(a)
