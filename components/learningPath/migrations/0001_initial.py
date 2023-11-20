# Generated by Django 4.2.1 on 2023-11-18 20:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('course', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='skillLearningPath',
            fields=[
                ('idSkills', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='tags',
            fields=[
                ('idTags', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='learningPath',
            fields=[
                ('idlearningPath', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('professionalRole', models.CharField(max_length=45)),
                ('pathScore', models.FloatField()),
                ('course', models.ManyToManyField(to='course.course')),
                ('idStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
                ('skill', models.ManyToManyField(to='learningPath.skilllearningpath')),
                ('tag', models.ManyToManyField(to='learningPath.tags')),
            ],
        ),
    ]
