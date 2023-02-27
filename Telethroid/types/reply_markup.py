from typing import List, Union
from Telethroid.types import InlineButtons

class ReplyMarkup:
    def __init__(self, keyboard=None, inline_keyboard=None, resize_keyboard=False, one_time_keyboard=False):
        self.keyboard = keyboard
        self.inline_keyboard = inline_keyboard
        self.resize_keyboard = resize_keyboard
        self.one_time_keyboard = one_time_keyboard

    def to_dict(self):
        reply_markup = {}
        if self.keyboard:
            reply_markup["keyboard"] = self.keyboard
        if self.inline_keyboard:
            reply_markup["inline_keyboard"] = self.inline_keyboard
        if self.resize_keyboard:
            reply_markup["resize_keyboard"] = self.resize_keyboard
        if self.one_time_keyboard:
            reply_markup["one_time_keyboard"] = self.one_time_keyboard
        return reply_markup
