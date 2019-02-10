import os
import requests
import json


class TelegramBot():

    def __init__(self):
        self.token = os.getenv("BOT_API_TOKEN")
        self.base_url = f"https://api.telegram.org/bot{self.token}/"

    def get_updates(self, offset=None):
        url = f"{self.base_url}getUpdates?timeout=100"
        if offset:
            url = f"{url}&offset={offset + 1}"
        r = requests.get(url)
        return json.loads(r.content)

    def send_message(self, msg, chat_id):
        url = f"{self.base_url}sendMessage?chat_id={chat_id}&text={msg}&parse_mode=Markdown"  # noqa E501
        if msg is not None:
            requests.get(url)
