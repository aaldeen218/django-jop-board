# Generated by Django 4.2.4 on 2023-08-19 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0028_alter_check_p_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subtest',
            name='sub_normal',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
