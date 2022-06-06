import json
from typing import Optional


class Messages:

    @classmethod
    async def read(cls):
        try:
            with open('./modules/messages/texts.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            raise TypeError('File by this dir was not found.')

    @staticmethod
    async def find_text(type_: Optional[str] = None):
        if type_ is None:
            return 'Помилка: текстова помилка'

        texts = await Messages.read()
        try:
            return texts['texts'][type_]
        except KeyError:
            return 'Помилка: текстова помилка'
