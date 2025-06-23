from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from database import database
from models import users, passes, images
import datetime
from contextlib import asynccontextmanager

class DatabaseManager:
    def __init__(self, database):
        self.database = database

    async def connect(self):
        await self.database.connect()

    async def disconnect(self):
        await self.database.disconnect()

    async def execute(self, query):
        return await self.database.execute(query)


class UserService:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    async def create_user(self, user_data: dict):
        query = users.insert().values(
            email=user_data["email"],
            fam=user_data["fam"],
            name=user_data["name"],
            otc=user_data.get("otc"),
            phone=user_data["phone"]
        )
        user_id = await self.db.execute(query)
        return user_id


class PassService:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    async def create_pass(self, pass_data: dict, user_id: int):
        coords = pass_data["coords"]
        level = pass_data["level"]
        add_time = datetime.datetime.strptime(pass_data.get("add_time"), "%Y-%m-%d %H:%M:%S")

        query = passes.insert().values(
            status = pass_data.get("status"),
            beauty_title=pass_data.get("beauty_title"),
            title=pass_data.get("title"),
            other_titles=pass_data.get("other_titles"),
            connect=pass_data.get("connect"),
            add_time=add_time,
            latitude=coords.get("latitude"),
            longitude=coords.get("longitude"),
            height=coords.get("height"),
            level_winter=level.get("winter"),
            level_summer=level.get("summer"),
            level_autumn=level.get("autumn"),
            level_spring=level.get("spring"),
            user_id=user_id
        )
        pass_id = await self.db.execute(query)
        return pass_id


class ImageService:
    def __init__(self, db_manager: DatabaseManager):
        self.db = db_manager

    async def add_images(self, images_data: list, pass_id: int):
        for img in images_data:
            query = images.insert().values(
                data=img.get("data"),
                title=img.get("title"),
                pass_id=pass_id
            )
            await self.db.execute(query)


class SubmitDataAPI:
    def __init__(self, user_service: UserService, pass_service: PassService, image_service: ImageService):
        self.user_service = user_service
        self.pass_service = pass_service
        self.image_service = image_service

    async def submit_data(self, request: Request):
        try:
            data = await request.json()
            required_fields = ["beauty_title", "title", "user", "coords", "level", "images", "add_time"]
            for field in required_fields:
                if field not in data:
                    return JSONResponse(status_code=400, content={"status": 400, "message": f"Field '{field}' is required", "id": None})

            user_id = await self.user_service.create_user(data["user"])
            pass_id = await self.pass_service.create_pass(data, user_id)
            await self.image_service.add_images(data.get("images", []), pass_id)

            return {"status": 200, "message": None, "id": pass_id}

        except Exception as e:
            return JSONResponse(status_code=500, content={"status": 500, "message": str(e), "id": None})


# Инициализация и запуск приложения

@asynccontextmanager
async def lifespan(app: FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)

db_manager = DatabaseManager(database)
user_service = UserService(db_manager)
pass_service = PassService(db_manager)
image_service = ImageService(db_manager)
submit_api = SubmitDataAPI(user_service, pass_service, image_service)


@app.post("/submitData")
async def submit_data_endpoint(request: Request):
    return await submit_api.submit_data(request)