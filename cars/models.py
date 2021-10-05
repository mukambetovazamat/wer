from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()


class Car(models.Model):
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Цена')
    name = models.CharField(verbose_name='Название машины', max_length=50)
    color = models.CharField(verbose_name='Цвет машины', max_length=50)
    motor = models.CharField(verbose_name='Объем двигателя', max_length=50)
    drive_unit = models.CharField(verbose_name='Привод машины', max_length=50)
    fuel_type = models.CharField(verbose_name='Тип топлива', max_length=50)
    image = models.ImageField(verbose_name='Изображение', upload_to='images/')
    car_owner = models.ForeignKey(User, verbose_name='Владелец', on_delete=models.CASCADE)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.name
