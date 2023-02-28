#  Telethroid - Telegram BoT Library for Python
#  Copyright (C) 2023-present Pr0fess0r-99 <https://github.com/Pr0fess0r-99>

import threading
import base64
import hashlib
import hmac
import urllib.parse
import urllib.request
import platform
import requests
import json
import time

# Telethroid
from Telethroid.types.message import Msg

class TelethroidClient:
    """
    A client class for interacting with the Telegram Bot API.

    Parameters:
        token (str): The Telegram bot token.
        api_id (int): The Telegram API ID for your app.
        api_hash (str): The Telegram API hash for your app.
        session (str): The string session for the userbot client (optional).

    Methods:
        send_message(chat_id: int, text: str) -> dict:
            Sends a message to the specified chat.

        get_updates() -> list:
            Retrieves new updates from the Telegram API.

        start_polling(handler) -> None:
            Continuously polls the Telegram API for updates and calls a handler function for each update.

        run() -> None:
            Starts the bot client.
    """

    def __init__(self, token: str, api_id: int, api_hash: str, session: str = None):
        self.token = token
        self.api_id = api_id
        self.api_hash = api_hash
        self.base_url = f"https://api.telegram.org/bot{token}/"
        self.last_update_id = 0
        self.session = session

    def send_message(self, chat_id: int, text: str) -> dict:
        """
        Sends a message to the specified chat.

        Parameters:
            chat_id (int): The ID of the chat to send the message to.
            text (str): The text of the message to send.

        Returns:
            dict: The response from the Telegram API.
        """
        url = f"{self.base_url}sendMessage"
        data = {"chat_id": chat_id, "text": text}
        response = requests.post(url, data=data)
        return json.loads(response.content)

    def get_updates(self) -> list:
        """
        Retrieves new updates from the Telegram API.

        Returns:
            list: A list of updates from the Telegram API.
        """
        url = f"{self.base_url}getUpdates"
        params = {"offset": self.last_update_id + 1, "timeout": 30}
        response = requests.get(url, params=params)
        return json.loads(response.content)

    def start_polling(self, handler):
        """
        Continuously polls the Telegram API for updates and calls a handler function for each update.

        Parameters:
            handler (function): A function that will be called with each new update.
        """
        while True:
            try:
                updates = self.get_updates()
                if len(updates) > 0:
                    self.last_update_id = updates[-1]['update_id']
                    for update in updates:
                        handler(update)
            except Exception as e:
                print(f"Error: {e}")
            time.sleep(1)

    def run(self):
        """
        Starts the bot client.
        """
        if self.session:
            from Telethroid import TelegramClient

            client = TelegramClient(self.session, self.api_id, self.api_hash)
            client.start()
        else:
            self.start_polling(self.handle_update)

    def handle_update(self, update):
        """
        Handles a single update from the Telegram API.

        Parameters:
            update (dict): A dictionary representing the update.
        """
        if "message" in update:
            message = message.Msg(update["message"])
            if filters.command("start")(message):
                self.send_message(
                    message.chat_id, "Hello, World!")
