from django.contrib.auth.models import AbstractUser
from django.db import models



# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name="Почта", help_text="укажите почту")
    number = models.CharField(max_length=40, blank=True, help_text="Номер телефона", null=True)
    town = models.CharField(max_length=40, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, help_text="Аватар", null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"