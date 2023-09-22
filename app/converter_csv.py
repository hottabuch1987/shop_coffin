import csv
import os
import django




os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from products.models import Category





filename = 'data.csv'

def load_data():
    data = [] # Список для хранения данных

    with open('/Users/hottabych/PycharmProjects/test_project/project14/app/data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['name']
            slug = row['slug']
          

            # Создание экземпляра Feedback и сохранение в базе данных
            feed = Category(name=name, slug=slug)
            feed.save()

            # Добавление данных в список
            data.append([name, slug])

    return data

if __name__ == '__main__':


    # Вызов функции load_data() и запись данных в файл
    data = load_data()

    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print('Файл CSV успешно создан и заполнен.')
