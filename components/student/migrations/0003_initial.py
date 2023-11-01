# Generated by Django 4.2.6 on 2023-11-01 18:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('student', '0002_remove_petition_idstudent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('idStudent', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('age', models.IntegerField()),
                ('email', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='skillStudent',
            fields=[
                ('idSkillStudent', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('idStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='petition',
            fields=[
                ('idPetition', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField()),
                ('topic', models.CharField(max_length=45)),
                ('description', models.CharField(max_length=200)),
                ('goal', models.CharField(max_length=200)),
                ('idStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
        migrations.CreateModel(
            name='interest',
            fields=[
                ('idInterest', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=45)),
                ('idStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.student')),
            ],
        ),
    ]