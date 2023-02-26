from typing import Any
from io import BytesIO

class Msg:
    def __init__(self, message_id: int, chat_id: int, text: str):
        self.id = message_id
        self.chat_id = chat_id
        self.text = text

    def __str__(self):
        return f"Message {self.id} in chat {self.chat_id}: {self.text}"
        
    @staticmethod
    def write(out: BytesIO, message: 'Msg'):
        out.write(int.to_bytes(message.id, length=4, byteorder='little', signed=True))
        out.write(int.to_bytes(message.chat_id, length=4, byteorder='little', signed=True))
        out.write(message.text.encode('utf-8'))

    @staticmethod
    def read(data: bytes) -> 'Msg':
        message_id = int.from_bytes(data[0:4], byteorder='little', signed=True)
        chat_id = int.from_bytes(data[4:8], byteorder='little', signed=True)
        text = data[8:].decode('utf-8')
        return Msg(message_id, chat_id, text)

    @staticmethod
    def import_(data: Any) -> 'Msg':
        if isinstance(data, bytes):
            return Msg.read(data)
        elif isinstance(data, dict):
            return Msg(data['id'], data['chat_id'], data['text'])
        else:
            raise ValueError("Invalid data type for Message import")
