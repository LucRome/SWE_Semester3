# Generated by Django 3.1.7 on 2021-04-21 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20210408_0854'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='description',
            field=models.TextField(default=None),
        ),
    ]
