# Generated by Django 3.2.3 on 2021-05-28 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_alter_signup_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='password',
            field=models.CharField(max_length=45),
        ),
    ]
