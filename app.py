from fastapi import FastAPI
from routes.user import user

app = FastAPI(
        title="API with mongodb",
        description="some basic CRUD urls learning Nosql"
)
app.include_router(user)
    