import jsonschema
import requests

schema = {'$schema': 'http://json-schema.org/schema#', 'type': 'array',
    'items': {'type': 'object',
    'properties': {
    'id': {'type': 'integer'},
    'title': {'type': 'string'},
    'description': {'type': 'string'},
    'excerpt': {'type': 'string'},
    'publishDate': {'type': 'string'}},
    'required': ['description', 'excerpt', 'id', 'publishDate', 'title'],
    'additionalProperties': False}}

def test_GET_book_schema_additional_properties():
    """
    В тесте проверяется, что ответ соответствует json-схеме.
    Тест выдаст ошибку, так как в ответе есть поле, которого нет в схеме.
    Поле additionalProperties определяет, могут ли в ответе быть поля, неуказанные в схеме.
    """
    response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Books')
    jsonschema.validate(instance=response.json(), schema=schema)
