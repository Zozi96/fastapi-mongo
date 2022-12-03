from fastapi import FastAPI
from motor import motor_asyncio
from motor.core import AgnosticCollection

USERNAME: str = "zozi"
PASSWORD: str = "Zozifer96"
HOST: str = "testing.1lksfd2.mongodb.net"

DB_URI: str = (
    f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOST}/test?retryWrites=true&w=majority"
)

client = motor_asyncio.AsyncIOMotorClient(DB_URI)

db = client.get_database("test")

user_collection: type[AgnosticCollection] = db.get_collection("users")

