# Генератор JSON-схем

### Используемые библиотеки
* json (входит в стандартные библиотеки Python, не требует дополнительной установки);
* [requests](https://requests.readthedocs.io/en/latest/);
* (pytest)[https://docs.pytest.org/en/7.1.x/contents.html];
* [genson](https://github.com/wolverdude/GenSON).

## Запуск проекта локально
На компьютере должен быть установлен Python. Инструкция по установке: 
[Windows](https://metanit.com/python/tutorial/1.2.php),
[MacOS](https://metanit.com/python/tutorial/1.5.php),
[Linux](https://metanit.com/python/tutorial/1.6.php).

Запустить терминал. Ввести команду, чтобы скопировать проект к себе на компьютер (будет скопирован в текущую папку):
```commandline
git clone https://github.com/mifologic/JSONSchemaGenerator.git
```

### Запуск из командной строки
Файлы можно запустить из терминала. Для запуска папки json_from_request потребуется установить библиотеку requests. 
Команда для установки:
````commandline
python -m pip install -r requirements.txt
````
**NB!** В некоторых операционных системах python может запускаться другой командой, например, python3. 

Чтобы запустить файлы из папки, нужно в терминале перейти в эту папку. После этого ввести команду:
```commandline
python file_name.py
```
Вместо file_name указать имя нужного файла.

Или для запуска всех файлов ввести команду (macOS, Linux):
```commandline
ls *.py|xargs -n 1 -P 4 python
```

### Запуск тестов
Запустить тесты в папке *json_schema_test_example* можно следующей командой:
```commandline
pytest file_name.py
```
Например:
```commandline
pytest test_GET_book_schema.py
```
### Другие варианты запуска
Также код можно открыть в удобной вам среде разработки, поддерживающей Python. 
Для запуска может потребоваться виртуальное окружение. Подробнее о нём можно почитать [здесь](https://pavel-karateev.gitbook.io/intermediate-python/sredstva-razrabotki/virtual_environment). 
