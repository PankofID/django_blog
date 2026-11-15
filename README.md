# Personal Blog on Django

Личный сайт-блог на фреймворке **Django**

---

![Скриншот главной страницы сайта](screenshots/screen.png)

Планируемое (to be):
* Возможность создавать посты с несколькими категориями

---

## Установка и запуск

### Шаг 1. Клонирование репозитория

```bash
git clone https://github.com/PankofID/django_blog.git
cd django_blog
```
---

### Шаг 2. Создание виртуального окружения

```bash
python -m venv venv
```

Windows:
```bash
venv\Scripts\activate
```
Linux/MacOS:
```bash
source venv/bin/activate
```

---

### Шаг 3. Установка зависимостей

```bash
pip install -r requirements.txt
```
---

### Шаг 4. Настройка `.env`

В терминале выполните:

```bash
cp .env.example .env
```
После в файле .env замените значения переменных на свои.

---

### Шаг 5. Миграции

В терминале выполните миграции:

```bash
python manage.py migrate
```

---

### Шаг 6. Запуск локального сервера

```bash
python manage.py runserver
```

Появится локальная ссылка:

```text
Starting development server at http://127.0.0.1:8000/
```

Если ошибок нет - откройте ссылку.