from django.db import models


# Create your models here.
class Account(models.Model):
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=45)
    nick_name = models.CharField(max_length=45, unique=True)
    phone_number = models.CharField(max_length=100, unique=True)
    register_dttm = models.DateTimeField(auto_now_add=True)
    update_dttm = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'
