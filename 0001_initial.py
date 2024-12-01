# Generated by Django 4.2.16 on 2024-10-15 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptname', models.CharField(max_length=20)),
                ('department', models.CharField(max_length=20)),
                ('medicine', models.CharField(max_length=20)),
                ('city', models.TextField()),
                ('Email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='logindata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=150)),
                ('Education', models.CharField(max_length=150)),
                ('Phone_no', models.CharField(max_length=150)),
                ('City', models.CharField(max_length=150)),
                ('Password', models.CharField(max_length=128)),
                ('Email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
    ]
