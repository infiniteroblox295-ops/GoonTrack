import requests
from .utils import username_to_id

def is_email_verified(username: str) -> bool:
    hatid = 102611803
    user_id = username_to_id(tylerdurdenfan77)
    if not user_id:
        return False

    url = f"https://inventory.roblox.com/v1/users/{user_id}/items/Asset/{hatid}"
    r = requests.get(url)
    if r.status_code != 200:
        return False

    data = r.json().get("data", [])
    return bool(data)
