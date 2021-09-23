import json
import os.path


class Tools:


    "Путь к словарю JSON"

    with open(os.path.abspath('data1.json'), encoding='utf-8-sig') as data:
        data = json.load(data)
