from datetime import datetime

from pydantic import BaseModel

class RepositoryShemas(BaseModel):
    name: str
    data_created: datetime
