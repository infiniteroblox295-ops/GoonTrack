import requests
from .utils import username_to_id

def get_full_body_thumbnail(username: str) -> str:
    user_id = username_to_id(username)
    if not user_id:
        return None
    url = f"https://thumbnails.roblox.com/v1/users/avatar?userIds={user_id}&size=420x420&format=Png&isCircular=false"
    r = requests.get(url)
    data = r.json()
    if "data" in data and len(data["data"]) > 0:
        return data["data"][0]["imageUrl"]
    return None