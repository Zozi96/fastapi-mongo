from decouple import config
from motor import motor_asyncio
from motor.core import AgnosticCollection

USERNAME = config("MONGO_USERNAME", cast=str)
PASSWORD = config("MONGO_PASSWORD", cast=str)
HOST = config("MONGO_HOST", cast=str)

DB_URI: str = (
    f"mongodb+srv://{USERNAME}:{PASSWORD}@{HOST}/test?retryWrites=true&w=majority"
)

client = motor_asyncio.AsyncIOMotorClient(DB_URI)

db = client.get_database("test")

user_collection: type[AgnosticCollection] = db.get_collection("users")

