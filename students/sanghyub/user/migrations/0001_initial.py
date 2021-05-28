# Generated by Django 3.2.3 on 2021-05-28 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=80)),
                ('password', models.CharField(max_length=30)),
                ('nickname', models.CharField(max_length=30)),
                ('phone_number', models.CharField(max_length=13)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]
