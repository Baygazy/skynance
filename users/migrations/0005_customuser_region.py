# Generated by Django 3.0.2 on 2020-02-07 09:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
        ('users', '0004_auto_20200207_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='region',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='region.Region'),
            preserve_default=False,
        ),
    ]
