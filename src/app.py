from fastapi import FastAPI

from .views import router

def create_app() -> FastAPI:
    app = FastAPI(title=" client tutorial",
                  version='2.2.8',
                  debug=True)
    app.include_router(router)
    return app
app = create_app()