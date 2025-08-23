import requests

def username_to_id(username):
    r = requests.post("https://users.roblox.com/v1/usernames/users", json={"usernames": [username]})
    r.raise_for_status()
    data = r.json().get("data", [])
    return data[0]["id"] if data else None