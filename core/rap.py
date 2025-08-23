import requests

def get_user_rap(user_id):
    url = f"https://inventory.roblox.com/v1/users/{user_id}/assets/collectibles?sortOrder=Asc&limit=100"
    rap = 0
    cursor = None

    while True:
        params = {"cursor": cursor} if cursor else {}
        r = requests.get(url, params=params)
        if r.status_code != 200:
            break
        data = r.json()
        for item in data.get("data", []):
            rap += item.get("recentAveragePrice", 0)
        cursor = data.get("nextPageCursor")
        if not cursor:
            break

    return rap