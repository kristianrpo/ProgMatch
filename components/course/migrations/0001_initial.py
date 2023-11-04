# Generated by Django 4.2.6 on 2023-11-04 04:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '__first__'),
        ('learningPath', '__first__'),
        ('institution', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('idCourse', models.AutoField(primary_key=True, serialize=False)),
                ('courseCode', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=45)),
                ('price', models.FloatField()),
                ('modality', models.CharField(max_length=45)),
                ('content', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('idInstitution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.institution')),
                ('idLearningPath', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learningPath.learningpath')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('idReview', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('content', models.CharField(max_length=200)),
                ('creationDate', models.DateField()),
                ('modificationDate', models.DateField(null=True)),
                ('idCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('idStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
