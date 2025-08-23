import requests
from .utils import username_to_id

def get_last_location(username: str) -> str | None:
    user_id = username_to_id(username)
    if not user_id:
        return None

    url = "https://presence.roblox.com/v1/presence/users"
    resp = requests.post(url, json={"userIds": [user_id]})
    if resp.status_code != 200:
        return None

    data = resp.json().get("userPresences", [])
    if not data:
        return None

    return data[0].get("lastLocation")