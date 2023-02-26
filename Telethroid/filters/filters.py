import requests
import json


def is_group(update):
    return 'message' in update and 'chat' in update['message'] and 'type' in update['message']['chat'] and update['message']['chat']['type'] == 'group'

def is_channel(update):
    return 'message' in update and 'chat' in update['message'] and 'type' in update['message']['chat'] and update['message']['chat']['type'] == 'channel'

def is_user(update, user_id):
    return 'message' in update and 'from' in update['message'] and 'id' in update['message']['from'] and update['message']['from']['id'] == user_id

def contains_hello(update):
    return 'message' in update and 'text' in update['message'] and 'hello' in update['message']['text'].lower()

def group_hello_handler(update):
    if is_group(update) and contains_hello(update):
        send_message(update['message']['chat']['id'], 'Hello group members!')

def channel_hello_handler(update):
    if is_channel(update) and contains_hello(update):
        send_message(update['message']['chat']['id'], 'Hello channel subscribers!')

def user_hello_handler(update, user_id):
    if is_user(update, user_id) and contains_hello(update):
        send_message(update['message']['chat']['id'], 'Hello, how can I help you?')

def text_handler(update):
    if 'message' in update and 'text' in update['message']:
        send_message(update['message']['chat']['id'], f"You said: {update['message']['text']}")



