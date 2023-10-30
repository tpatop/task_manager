from api.models.user import UserInDB

fake_db = {
    "user": {
        "username": "user",
        "hash_password": "$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "active": True,
    }
}


def get_user(username: str):
    if username in fake_db:
        user = fake_db.get(username)
        return UserInDB(**user)
