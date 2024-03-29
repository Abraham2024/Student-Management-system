# Generated by Django 4.2.6 on 2024-01-12 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Student_name', models.PositiveIntegerField()),
                ('First_name', models.CharField(max_length=50)),
                ('Last_name', models.CharField(max_length=50)),
                ('Email', models.EmailField(max_length=50)),
                ('Field_of_study', models.CharField(max_length=50)),
                ('gpa', models.FloatField()),
            ],
        ),
    ]
