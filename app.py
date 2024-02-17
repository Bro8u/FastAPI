import fastapi
import pydantic_models
from typing import Annotated
from fastapi import Request, Query
import config

app = fastapi.FastAPI()

response = {"her, pizda, ochko"}
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


@app.put("/change_user_by_id/{id}")
def change_user_by_id(id: int, user: pydantic_models.User = fastapi.Body()):
    for index, u in enumerate(fake_database['users']):
        if u['id'] == id:
            fake_database['users'][index] = user
            return user
@app.delete("/delete_user_by_id/{id}")
def change_user_by_id(id: int):
    for index, u in enumerate(fake_database['users']):
        if u['id'] == id:
            old_user = fake_database['users'][index]
            del fake_database['users'][index]
            return {"old_user": old_user, "new_db":fake_database['users']}

@app.get("/query")
def query(q: Annotated[int | str | None, Query(max_length=5)] = None):
    if q:
        print({"q": q})
    return q
@app.get("/")
@app.post("/")
@app.put("/")
@app.delete("/")
def index(request: Request):
    return {"Request": [request.method, request.headers]}
@app.post("/create/user")
def create(user: pydantic_models.User):
    fake_database['users'].append(user)
    print(len(fake_database['users']))
    return {'User_created':user}

@app.get("/user_balance/{id}")
def user_balance(id: int):
    return fake_database["users"][id]["balance"]
@app.get("/user_info/{id}")
def user_info(id : int):
    return fake_database["users"][id]
@app.get("/total_balance")
def total_balance():
    balance_sum: float = 0.0
    for user in fake_database["users"]:
        balance_sum += pydantic_models.User(**user).balance
    return balance_sum

@app.get("/slice")
def slice(limit: int, skip: int = 0):
    return fake_database["users"][skip: skip + limit]

