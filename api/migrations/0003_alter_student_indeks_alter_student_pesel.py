# Generated by Django 4.0.4 on 2022-04-24 12:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_student_indeks_alter_student_pesel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='indeks',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxLengthValidator(100000), django.core.validators.MinLengthValidator(999999)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='pesel',
            field=models.PositiveIntegerField(unique=True, validators=[django.core.validators.MaxLengthValidator(10000000000), django.core.validators.MinLengthValidator(99999999999)]),
        ),
    ]
