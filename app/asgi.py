from uvicorn import run

from fastapi import FastAPI, responses
from core.settings import API
from core.routers.users import router as users_router

app = FastAPI(**API)


@app.get("/")
async def root():
    return responses.RedirectResponse(url="/docs")


app.include_router(users_router, prefix="/api")
