# Generated by Django 4.2.6 on 2023-11-01 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='idCourse',
        ),
        migrations.RemoveField(
            model_name='review',
            name='idStudent',
        ),
        migrations.DeleteModel(
            name='course',
        ),
        migrations.DeleteModel(
            name='review',
        ),
    ]
