### Test Project
[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%2336BCF7&lines=Django+Test+Project)](https://git.io/typing-svg)

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

![Image alt](https://github.com/hottabuch1987/shop_coffin/raw/document/img/1.png)
![Image alt](https://github.com/hottabuch1987/shop_coffin/raw/document/img/2.png)
![Image alt](https://github.com/hottabuch1987/shop_coffin/raw/document/img/3.png)






