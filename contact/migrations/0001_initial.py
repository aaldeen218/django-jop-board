# Generated by Django 4.2.3 on 2023-08-10 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('Subject', models.CharField(max_length=50)),
                ('Message', models.TextField(max_length=5000)),
            ],
        ),
    ]