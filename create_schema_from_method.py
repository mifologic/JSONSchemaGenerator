import requests

from genson import SchemaBuilder


def create_json_schema(method):
    """Создаёт json-схему из переданных данных
    :param method: ссылка для вызова метода
    :return: сгенерированная json-схема
    """
    response = requests.get(method)  # вызываем метод и получаем ответ
    builder = SchemaBuilder()   # создаём объект SchemaBuilder и сохраняем в переменную
    builder.add_object(response.json())  # вызываем у SchemaBuilder метод add_object и на вход передаём ответ метода в json
    return builder.to_schema()      # возвращаем ответ в виде автоматически сгенерированной json-схемы


print("Сгенерирована схема: ")
print(create_json_schema('https://fakerestapi.azurewebsites.net/api/v1/Books'))  # печатаем схему
