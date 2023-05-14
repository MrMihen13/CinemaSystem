# Cinema System

## Local development

Для запуска проекта необходимо поднять `Docker` контейнер
```shell
docker-compose up
```

Для создания суперпользователя, внутри контейнера нужно ввести команду
```shell
python manage.py createsuperuser
```

Админка доступна по ссылке
```djangourlpath
http://127.0.0.1:8000/admin/
```

Документация 
```djangourlpath
http://localhost:8000/api/v1/swagger/
```

```djangourlpath
http://localhost:8000/api/v1/redoc/
```