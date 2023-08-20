# Generated by Django 4.2.4 on 2023-08-19 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0027_alter_check_p_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='p_name',
            field=models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='p_check', to='tests.patient'),
        ),
    ]