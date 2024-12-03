from sqlalchemy import Table, Column
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import Boolean, Integer, String, Text, UUID

from config.connectdb import meta, engine

users = Table(
    "users",
    meta,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("username", String(255)),
    Column("email", String(255)),
    Column("password", String(255)),
    Column("is_active", Boolean),
)

meta.create_all(engine)