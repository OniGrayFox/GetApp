# Generated by Django 3.2.12 on 2023-05-10 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('surname', models.CharField(max_length=100, verbose_name='Surname')),
            ],
            options={
                'verbose_name': 'UserInfo',
                'verbose_name_plural': 'UsersInfo',
            },
        ),
    ]
