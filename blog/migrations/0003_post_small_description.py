# Generated by Django 3.0.5 on 2020-06-15 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20200614_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='small_description',
            field=models.CharField(default='', max_length=200),
        ),
    ]
