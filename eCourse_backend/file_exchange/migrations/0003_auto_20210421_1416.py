# Generated by Django 3.1.7 on 2021-04-21 14:16

from django.db import migrations, models
import file_exchange.models


class Migration(migrations.Migration):

    dependencies = [
        ('file_exchange', '0002_remove_submission_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='file',
            field=models.FileField(
                upload_to=file_exchange.models.exercise_directory_path,
                validators=[
                    file_exchange.models.validate_file_type]),
        ),
    ]
