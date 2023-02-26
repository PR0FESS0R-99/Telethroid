from typing import List, Union
from Telethroid.types import InlineButtons

class ReplyMarkup:
    @staticmethod
    def inline_keyboard(buttons: List[List[dict]]) -> dict:
        inline_buttons = InlineButtons()
        for row in buttons:
            inline_buttons.add_row(row)

        return inline_buttons.to_dict()
