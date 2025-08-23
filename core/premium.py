import requests
from .utils import username_to_id

def is_premium(username: str) -> bool:
    user_id = username_to_id(username)
    if not user_id:
        return False

    url = f"https://premiumfeatures.roblox.com/v1/users/{user_id}/validate-membership"
    r = requests.get(url)
    if r.status_code != 200:
        return False

    return r.json().get("isPremium", False)