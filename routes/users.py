from fastapi import APIRouter
from config.connectdb import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
user = APIRouter()

key = Fernet.generate_key()
unique_key = Fernet(key)

@user.get("/users")
async def get_users():
    try:
        result = conn.execute(users.select()).fetchall()
        if len(result) == 0:
            return {"message": "No records found"}
        elif len(result) > 0:
            return {"data": dict(result[0])}
    except Exception as e:
        return {"error": str(e)}
    

@user.post("/users")
async def create_users(user: User):
    try:
        new_user = {"username": user.username,"email": user.email ,"is_active": user.is_active }
        new_user["password"] = unique_key.encrypt(user.password.encode("utf-8"))
        result = conn.execute(users.insert().values(new_user))
        print(new_user)
    except Exception as e:
        print(e)
        print(result)
        return {"error": str(e)} 
    return result # conn.execute(users.select().where(users.c.id == result.lastrowid)).first()



@user.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"username": "Rick"}


@user.put("/users")
async def update_users():
    return {"message": "User updated successfully"}

@user.delete("/users")
async def delete_users():
    return {"message": "User deleted successfully"}

