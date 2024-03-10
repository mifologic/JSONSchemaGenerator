import json

from genson import SchemaBuilder

"""
* Шаг 1.
Сохраняем json в переменную.
"""

json_data = """[
  {
    "id": 1,
    "title": "Activity 1",
    "dueDate": "2024-01-09T19:03:43.1718735+00:00",
    "completed": false
  },
  {
    "id": 2,
    "title": "Activity 2",
    "dueDate": "2024-01-09T20:03:43.1718764+00:00",
    "completed": true
  },
  {
    "id": 3,
    "title": "Activity 3",
    "dueDate": "2024-01-09T21:03:43.1718768+00:00",
    "completed": false
  },
  {
    "id": 4,
    "title": "Activity 4",
    "dueDate": "2024-01-09T22:03:43.1718771+00:00",
    "completed": true
  },
  {
    "id": 5,
    "title": "Activity 5",
    "dueDate": "2024-01-09T23:03:43.1718774+00:00",
    "completed": false
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
print(builder.to_schema())
