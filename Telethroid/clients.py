#  Telethroid - Telegram BoT Library for Python
#  Copyright (C) 2023-present Pr0fess0r-99 <https://github.com/Pr0fess0r-99>

import threading
import base64
import hashlib
import hmac
import json
import time
import urllib.parse
import urllib.request
import platform

class TelethroidClientTool(object):
    DEVICE_MODEL = f"{platform.python_implementation()} {platform.python_version()}"

class TelethroidClient:
    "Telethroid Client"

    def __init__(
        self,
        api_id: int = None,
        api_hash: str = None,
        bot_token: str = None,
        string_session: str = None,
        phone_number: str = None,
        device_model: str= TelethroidClientTool.DEVICE_MODEL
    ):

        self.api_id = api_id
        self.api_hash = api_hash
        self.bot_token = bot_token
        self.string_session = string_session
        self.phone_code = phone_number
        self.device_model = device_model

        self.lock = threading.Lock()

    def send_request(self, method: str, params: dict, timeout: int = 30):
        with self.lock:
            url = f'https://api.telegram.org/bot{self.bot_token}/{method}'
            data = urllib.parse.urlencode(params).encode('utf-8')
            headers = {'Content-Type': 'application/x-www-form-urlencoded'}

            request = urllib.request.Request(url, data=data, headers=headers, method='POST')
            response = urllib.request.urlopen(request, timeout=timeout)

            return json.loads(response.read().decode('utf-8'))

    def get_auth_key(self):
        nonce = str(int(time.time()))
        data = nonce + self.api_id + self.api_hash + self.bot_token
        return base64.b64encode(hmac.new(self.phone_code.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).digest())

    def login(self):
        auth_key = self.get_auth_key()
        params = {'phone_code': self.phone_code, 'device_model': self.device_model, 'auth_key': auth_key}

        result = self.send_request('auth.login', params)
        if result.get('status') == 'ok':
            self.string_session = result.get('string_session')
            return True
        else:
            return False

    def check_auth(self):
        params = {'string_session': self.string_session}
        result = self.send_request('auth.check', params)
        if result.get('status') == 'ok':
            return True
        else:
            return False

    def send_message(self, chat_id: int, text: str):
        params = {'chat_id': chat_id, 'text': text}
        result = self.send_request('messages.send', params)
        if result.get('status') == 'ok':
            return True
        else:
            return False

    def handle_error(self, error: dict):
        if error.get('error_code') == 401:
            self.login()
        else:
            raise Exception(f'Telegram API error: {error}')

    def __call__(self, method: str, params: dict):
        params['string_session'] = self.string_session

        while True:
            try:
                result = self.send_request(method, params)
                if result.get('status') == 'ok':
                    return result.get('result')
                elif result.get('error'):
                    self.handle_error(result.get('error'))
                else:
                    raise Exception('Unexpected response from Telegram API')
            except Exception as e:
                print(f'Telegram API error: {e}')
                time.sleep(5)
