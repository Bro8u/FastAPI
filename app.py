import fastapi
import pydantic_models
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
        # print(type(user))
        balance_sum += pydantic_models.Users(**user).balance
    return balance_sum

@app.get("/slice/{id}")
def slice(limit: int, id: int, skip: int = 0):
    return fake_database["users"][skip: skip + limit][id]




