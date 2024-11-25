

python -m venv myproject
..\myproject\Scripts\activate

pip install Django 
django-admin startproject django_bongo
python manage.py runserver

Create App:
python manage.py startapp machine_learning

 python manage.py makemigrations
 python manage.py migrate

##################Save Data Shell Script###############
python manage.py shell

from machine_learning.models import *
student = Student(name="abcd",age=12,email="abc@gmail.com",address="Dhaka")
student.save()

car = Car(car_name="bazaj",speed=200)
car.save()


pip install -r requirements.txt