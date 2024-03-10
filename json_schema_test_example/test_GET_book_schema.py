import jsonschema
import requests

schema = {'$schema': 'http://json-schema.org/schema#', 'type': 'array',
    'items': {'type': 'object',
    'properties': {
    'id': {'type': 'integer'},
    'title': {'type': 'string'},
    'description': {'type': 'string'},
    'pageCount': {'type': 'integer'},
    'excerpt': {'type': 'string'},
    'publishDate': {'type': 'string'}},
    'required': ['description', 'excerpt', 'id', 'pageCount', 'publishDate', 'title'],
    'additionalProperties': False}}

def test_GET_book_schema():
    """
    В тесте проверяется, что ответ соответствует json-схеме.
    Поле additionalProperties определяет, могут ли в ответе быть поля, неуказанные в схеме.
    """
    response = requests.get('https://fakerestapi.azurewebsites.net/api/v1/Books')
    jsonschema.validate(instance=response.json(), schema=schema)
