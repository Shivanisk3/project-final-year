# Generated by Django 3.2.5 on 2021-07-05 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='id',
        ),
        migrations.AlterField(
            model_name='reg',
            name='email_address',
            field=models.EmailField(max_length=254, serialize=False),
        ),
    ]
