from fastapi import FastAPI
from app.routes.explain import router
from app.database import connection

app = FastAPI(title="Explain My Code API")

app.include_router(router)