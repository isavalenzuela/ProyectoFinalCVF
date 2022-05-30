# Generated by Django 4.0.4 on 2022-05-30 17:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0004_profesional_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='profesional',
            name='profRegion',
            field=models.CharField(default=django.utils.timezone.now, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profesional',
            name='workplace',
            field=models.CharField(default=1, max_length=300),
            preserve_default=False,
        ),
    ]