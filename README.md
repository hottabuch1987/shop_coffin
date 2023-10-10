### Магазин гробов
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Django+Vuejs+Магазин+Ритальных+услуг)](https://git.io/typing-svg)

### python3 -m venv venv
### source venv/bin/activate
### pip install -r requirements.txt

### python manage.py makemigrations
### python manage.py migrate
### python manage.py runserver

### new terminal, start redis 
docker run -p 127.0.0.1:16379:6379 --name redis-celery -d redis

### start celery
celery -A django_project worker -l info

### start vuejs
### npm install
### npm run serve

# backend проекта :
    - Пользовательская модель аутентификации, включающая электронную почту в качестве уникального идентификатора.
    - Интегрированна Celery для отправки OTP пользователям во время входа в систему.
    - Отправка 6-значного OTP-кода на электронную почту mail.ru пользователя и подтверждение его в течении 5 минут
    - Хранение паролей с использованием алгоритма хеширования Argon.
    - Документация Swagger.
# frontend проекта :
    - Vuex для хранения состояния
    - boolma для вывода сообщений








![Image alt](https://github.com/hottabuch1987/shop_coffin/raw/document/img/1.png)
![Image alt](https://github.com/hottabuch1987/shop_coffin/raw/document/img/2.png)
![Image alt](https://github.com/hottabuch1987/shop_coffin/raw/document/img/3.png)



