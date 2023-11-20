# Generated by Django 4.2.1 on 2023-11-18 20:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '__first__'),
        ('institution', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseCode', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=100)),
                ('length', models.CharField(max_length=45)),
                ('price', models.FloatField()),
                ('modality', models.CharField(max_length=45)),
                ('content', models.CharField(max_length=200, null=True)),
                ('description', models.TextField()),
                ('link', models.CharField(max_length=200)),
                ('difficulty', models.CharField(choices=[('facil', 'Fácil'), ('intermedio', 'Intermedio'), ('dificil', 'Difícil')], max_length=10)),
                ('idInstitution', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='institution.institution')),
            ],
        ),
        migrations.CreateModel(
            name='review',
            fields=[
                ('idReview', models.AutoField(primary_key=True, serialize=False)),
                ('score', models.IntegerField()),
                ('content', models.TextField()),
                ('creationDate', models.DateField()),
                ('modificationDate', models.DateField(null=True)),
                ('idCourse', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.course')),
                ('idStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]
