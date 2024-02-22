# import pydantic_models
# import app
# fake_database = {'users':[
#     {
#         "id":1,             # тут тип данных - число
#         "name":"Anna",      # тут строка
#         "nick":"Anny42",    # и тут
#         "balance": 15300    # а тут float
#      },
#     {
#         "id":2,             # у второго пользователя
#         "name":"Dima",      # такие же
#         "nick":"dimon2319", # типы
#         "balance": 160.23     # данных
#      }
#     ,{
#         "id":3,             # у третьего
#         "name":"Vladimir",  # юзера
#         "nick":"Vova777",   # мы специально сделаем
#         "balance": "25000"     # нестандартный тип данных в его балансе
#      }
# ],}
# id = 2
# user = {
#     "id":4,
#     "name": "debil",
#     "nick": "her",
#     "balance": 13.4
# }
#
# for index, u in enumerate(fake_database['users']):
#     if u['id'] == id:
#         fake_database['users'][index] = user
# print(fake_database['users'])
#
# a = app.query('j')
# print(a)

from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse

app = FastAPI()

html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="text" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input.value)
                input.value = ''
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""


@app.get("/")
async def get():
    return HTMLResponse(html)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")
