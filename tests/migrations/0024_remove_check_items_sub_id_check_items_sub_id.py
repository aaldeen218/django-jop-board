# Generated by Django 4.2.4 on 2023-08-19 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0023_check_items'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check_items',
            name='sub_id',
        ),
        migrations.AddField(
            model_name='check_items',
            name='sub_id',
            field=models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.DO_NOTHING, to='tests.subtest'),
            preserve_default=False,
        ),
    ]
