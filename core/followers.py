import requests
from .utils import username_to_id

def get_followers_count(username: str) -> int:
    user_id = username_to_id(username)
    if not user_id:
        return 0
    url = f"https://friends.roblox.com/v1/users/{user_id}/followers/count"
    r = requests.get(url)
    if r.status_code != 200:
        return 0
    return r.json().get("count", 0)

def get_following_count(username: str) -> int:
    user_id = username_to_id(username)
    if not user_id:
        return 0
    url = f"https://friends.roblox.com/v1/users/{user_id}/followings/count"
    r = requests.get(url)
    if r.status_code != 200:
        return 0
    return r.json().get("count", 0)