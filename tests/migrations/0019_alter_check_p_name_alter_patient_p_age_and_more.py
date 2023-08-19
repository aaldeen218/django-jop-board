# Generated by Django 4.2.4 on 2023-08-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0018_alter_check_p_name_alter_check_test_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='check',
            name='p_name',
            field=models.ForeignKey(default=1, max_length=50, on_delete=django.db.models.deletion.CASCADE, related_name='p_check', to='tests.patient'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='p_age',
            field=models.IntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='p_name',
            field=models.CharField(max_length=50, verbose_name='Patient Name'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='p_phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='p_sex',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default=1, max_length=50, verbose_name='Sex'),
        ),
    ]