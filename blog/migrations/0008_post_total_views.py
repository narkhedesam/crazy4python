# Generated by Django 3.0.5 on 2020-06-16 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200616_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='total_views',
            field=models.IntegerField(default=0),
        ),
    ]
