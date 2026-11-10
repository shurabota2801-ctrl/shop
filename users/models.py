from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomerUser(AbstractUser):

    class RoleCustomerUser(models.TextChoices):
        CUSTOMER = 'customer', 'Покупатель'
        MANAGER = 'manager', 'Менеджер'
        ADMIN = 'admin', 'Администратор'

    role = models.CharField(max_length=30, choices=RoleCustomerUser.choices, default=RoleCustomerUser.CUSTOMER, verbose_name='Роль')
    number_phone = models.CharField(max_length=20, blank=True, verbose_name='Телефон')
    birth_date = models.DateField(blank=True, null=True, verbose_name='День рождения')

    def __str__(self):
        return self.username

    @property
    def is_manager(self):
        return self.role == self.RoleCustomerUser.MANAGER

    @property
    def is_customer(self):
        return self.role == self.RoleCustomerUser.CUSTOMER
    
