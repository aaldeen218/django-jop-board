# Generated by Django 4.2.4 on 2023-08-18 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0010_alter_subtest_sub_normal_alter_subtest_sub_part'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtest',
            name='sub_normal',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
    ]
