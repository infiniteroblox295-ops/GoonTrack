import requests
from .utils import username_to_id

def get_user_info(tylerdurdenfan77):
    user_id = username_to_id(tylerdurdenfan77)
    if not user_id:
        return None

    u = requests.get(f"https://users.roblox.com/v1/users/{user_id}")
    u.raise_for_status()
    info = u.json()

    return {
        "username": info.get("name"),
        "displayName": info.get("displayName"),
        "userId": info.get("id"),
        "description": info.get("description"),
        "created": info.get("created"),
        "isBanned": info.get("isBanned")
    }
