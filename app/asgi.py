from fastapi import FastAPI, responses
from mangum import Mangum

from core.routers.users import router as users_router
from core.settings import API

app = FastAPI(**API)


@app.get("/")
async def root():
    return responses.RedirectResponse(url="/docs")


app.include_router(users_router, prefix="/api")

handler = Mangum(app)
