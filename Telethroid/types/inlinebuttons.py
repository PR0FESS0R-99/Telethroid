from typing import List, Union

class InlineButtons:
    def __init__(self, text: str = None, url: str = None, callback_data: str = None) -> None:
        self.buttons: List[List[dict]] = []
        if text is not None:
            self.add_button(text, url, callback_data)

    def add_button(self, text: str, url: str = None, callback_data: str = None) -> None:
        button: dict = {
            'text': text,
            'url': url,
            'callback_data': callback_data,
        }
        self.buttons.append([button])

    def add_row(self, row_buttons: List[dict]) -> None:
        row: List[dict] = []
        for button in row_buttons:
            row.append({
                'text': button['text'],
                'url': button.get('url'),
                'callback_data': button.get('callback_data'),
            })
        self.buttons.append(row)

    def to_dict(self) -> dict:
        return {'inline_keyboard': self.buttons}
