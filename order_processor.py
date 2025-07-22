import json
from instabot import login_bot, follow_user

BOT_USERNAME = "botkullaniciadi"
BOT_PASSWORD = "botsifresi"

def process_orders():
    with open("orders.json", "r") as f:
        order = json.load(f)

    username = order["username"]
    amount = order["amount"]

    cl = login_bot(BOT_USERNAME, BOT_PASSWORD)
    for _ in range(amount):
        follow_user(cl, username)

if __name__ == "__main__":
    process_orders()