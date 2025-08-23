from flask import Flask, jsonify
from core import (
    get_user_info,
    get_user_groups,
    get_owned_groups,
    username_to_id,
    get_user_rap,
    get_full_body_thumbnail,
    get_last_location,
    get_friends_count,
    is_email_verified,
    is_premium,
    get_followers_count,
    get_following_count
)

app = Flask(__name__)

@app.route("/user/<username>")
def user(username):
    user_data = get_user_info(username)
    if not user_data:
        return jsonify({"error": "user not found"}), 404

    user_id = username_to_id(username)
    if not user_id:
        return jsonify({"error": "could not resolve user id"}), 404

    groups = get_user_groups(username) or []
    owned = get_owned_groups(username) or []
    rap = get_user_rap(user_id)
    avatar_url = get_full_body_thumbnail(username)
    last_location = get_last_location(username)
    friends_count = get_friends_count(username)
    email_verified = is_email_verified(username)
    premium_status = is_premium(username)
    followers_count = get_followers_count(username)
    following_count = get_following_count(username)

    return jsonify({
        **user_data,
        "groups_joined": len(groups),
        "groups_owned": len(owned),
        "rap": rap,
        "avatar": avatar_url,
        "last_location": last_location,
        "friends_count": friends_count,
        "followers_count": followers_count,
        "following_count": following_count,
        "email_verified": email_verified,
        "premium": premium_status
    })

if __name__ == "__main__":
    app.run(debug=True)