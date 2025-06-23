from sqlalchemy import (
    Table, Column, Integer, String, ForeignKey, DateTime, MetaData, Text, Enum
)
import datetime

metadata = MetaData()

users = Table(
    "users", metadata,
    Column("id", Integer, primary_key=True),
    Column("email", String, nullable=False),
    Column("fam", String, nullable=False),
    Column("name", String, nullable=False),
    Column("otc", String, nullable=False),
    Column("phone", String, nullable=False),
)

passes = Table(
    "passes", metadata,
    Column("status",Enum("new","pending","accepted","rejected",name = "status")),
    Column("id", Integer, primary_key=True),
    Column("beauty_title", String),
    Column("title", String),
    Column("other_titles", String),
    Column("connect", String),
    Column("add_time", DateTime, default=datetime.datetime.utcnow),
    Column("latitude", String),
    Column("longitude", String),
    Column("height", String),
    Column("level_winter", String),
    Column("level_summer", String),
    Column("level_autumn", String),
    Column("level_spring", String),
    Column("user_id", Integer, ForeignKey("users.id")),
)

images = Table(
    "images", metadata,
    Column("id", Integer, primary_key=True),
    Column("data", Text),
    Column("title", String),
    Column("pass_id", Integer, ForeignKey("passes.id")),
)