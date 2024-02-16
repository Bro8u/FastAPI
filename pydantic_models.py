import pydantic
class Users(pydantic.BaseModel):
    id: int
    name: str
    nick: str
    balance: float

