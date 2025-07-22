from instagrapi import Client

def login_bot(username, password):
    cl = Client()
    cl.login(username, password)
    return cl

def follow_user(cl, target_username):
    user_id = cl.user_id_from_username(target_username)
    cl.user_follow(user_id)
    print(f"@{target_username} takip edildi.")