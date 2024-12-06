from fastapi import APIRouter, HTTPException
from config.connectdb import conn
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
import json
import logging
user = APIRouter()

key = Fernet.generate_key()
unique_key = Fernet(key)

@user.get("/users")
async def get_users():
    try:
        query = users.select()
        result = conn.execute(query)
        if result is None:
            return {"error": "Database it is empty, No users found"}
        else:
            result = [user.__dict__ for user in users]
            for user in result:
                user.pop("_sa_instance_state", None)
            return result
    except SQLAlchemyError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}
    

@user.post("/users")
async def create_users(user: User):
    try:
        new_user = {
            "username": user.username,
            "email": user.email,
            "is_active": user.is_active,
        }
        new_user["password"] = unique_key.encrypt(user.password.encode("utf-8"))
        result = conn.execute(users.insert().values(new_user))
        new_user_id = result.lastrowid
        conn.commit()
        return {"message": "User created successfully", "user_id": new_user_id}
    except SQLAlchemyError as e:
        return {"error": str(e)}
    except Exception as e:
        return {"error": str(e)}




@user.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"username": "Rick"}


@user.put("/users")
async def update_users():
    return {"message": "User updated successfully"}

@user.delete("/users")
async def delete_users():
    return {"message": "User deleted successfully"}

