# Generated by Django 3.0.2 on 2020-02-07 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
