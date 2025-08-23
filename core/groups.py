import requests
from .utils import username_to_id

def get_user_groups(username):
    user_id = username_to_id(username)
    if not user_id:
        return None

    g = requests.get(f"https://groups.roblox.com/v1/users/{user_id}/groups/roles")
    g.raise_for_status()
    groups = g.json().get("data", [])

    return [
        {
            "groupId": grp["group"]["id"],
            "groupName": grp["group"]["name"],
            "role": grp["role"]["name"]
        }
        for grp in groups
    ]

def get_owned_groups(username):
    groups = get_user_groups(username)
    if groups is None:
        return None
    return [
        {"groupId": g["groupId"], "groupName": g["groupName"]}
        for g in groups if g["role"].lower() == "owner"
    ]