import json

from genson import SchemaBuilder

"""
* Шаг 1.
Сохраняем json в переменную.
"""

json_data = """[
{
        "id": 1,
        "title": "Book 1",
        "description": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.",
        "pageCount": 100,
        "excerpt": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.",
        "publishDate": "2024-03-22T21:00:35.2216895+00:00"
    },
    {
        "id": 2,
        "title": "Book 2",
        "description": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.",
        "pageCount": 200,
        "excerpt": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.",
        "publishDate": "2024-03-21T21:00:35.221705+00:00"
    },
    {
        "id": 3,
        "title": "Book 3",
        "description": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.",
        "pageCount": 300,
        "excerpt": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.",
        "publishDate": "2024-03-20T21:00:35.2217163+00:00"
    },
    {
        "id": 4,
        "title": "Book 4",
        "description": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.",
        "pageCount": 400,
        "excerpt": "Lorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.nLorem lorem lorem. Lorem lorem lorem. Lorem lorem lorem.",
        "publishDate": "2024-03-19T21:00:35.221728+00:00"
    }
    ]
"""

"""
* Шаг 2.
Преобразуем json в python-объект.
"""
data_from_json = json.loads(json_data)

"""
* Шаг 3.
Сохраняем в переменную класс для генерации схем.
Вызываем у него метод add_object, в который передаём данные.
Выводим json-схему.
"""
builder = SchemaBuilder()
builder.add_object(data_from_json)
print("Сгенерирована схема: ")
print(builder.to_schema())
