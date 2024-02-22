from github import Github
from fastapi import Depends
from fastapi.routing import APIRoute, APIRouter
from .shemas import RepositoryShemas

from .dependencies import get_github_client


router = APIRouter(tags=['lalalend'])
@router.get('/get_reposit',
            summary='summary',
            description='description',
            response_model=RepositoryShemas)
def get_reposit(github_client: Github = Depends(get_github_client)):
    print(github_client)
    return RepositoryShemas(
        name='NameOfRepo',
        data_created='2010-01-01T00:00:00Z'
    )

