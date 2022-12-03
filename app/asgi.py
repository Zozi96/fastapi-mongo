from uvicorn import run

from fastapi import FastAPI, responses
from core.settings import API
from core.routers.users import router as users_router

app = FastAPI(**API)

@app.get("/")
async def root():
    return responses.RedirectResponse(url="/docs")

app.include_router(users_router, prefix="/api")

if __name__ == "__main__":
    run("asgi:app", host="0.0.0.0", port=5000, log_level="info", reload=True)
