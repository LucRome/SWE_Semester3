# Generated by Django 3.1.7 on 2021-04-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210415_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='user', name='type', field=models.IntegerField(
                choices=[
                    (1, 'Office'), (2, 'Lecturer'), (3, 'Student')], default=3), ), ]
