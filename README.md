#  FastAPI ToDo API

Цей проєкт — простий RESTful API для управління списком задач, реалізований на FastAPI. 
Він демонструє базові CRUD-операції, валідацію через Pydantic, зберігання даних у пам’яті та покриття тестами через pytest.

---

##  Технології

- **FastAPI** — фреймворк для створення API
- **Pydantic** — валідація даних
- **Pytest** — юніт-тести
- **httpx** — тестовий клієнт
- **In-memory storage** — список `tasks` у пам’яті

---

##  Встановлення

```bash
git clone https://github.com/your-username/fastapi-todo-api.git
cd fastapi-todo-api
python -m venv venv
source venv/bin/activate  # або venv\Scripts\activate на Windows
pip install -r requirements.txt
```

##  Запуск тестів
```bash
pytest tests/
```

## Запуск сервера
```bash
uvicorn app.main:app --reload
```
---
  Документація буде доступна за адресою: http://127.0.0.1:8000/docs
---

## Структура проєкту
fastapi_todo/
├── app/
│   ├── main.py         # Ендпоінти FastAPI
│   ├── models.py       # Pydantic моделі
│   ├── storage.py      # CRUD-логіка
├── tests/
│   └── test_api.py     # Юніт-тести
├── requirements.txt    # Залежності
├── README.md           # Опис проєкту
├── .gitignore          # Ігнорування службових файлів


## Реалізовані ендпоінти
Метод	Шлях	     Опис
GET	    /tasks	     Отримати список задач
POST	/tasks	     Створити нову задачу
PUT  	/tasks/{id}	 Оновити задачу за ID
DELETE	/tasks/{id}	 Видалити задачу за ID
