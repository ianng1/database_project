# Generated by Django 2.0.2 on 2018-09-10 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0018_auto_20180910_0530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthday',
            field=models.DateField(default='2000-01-01', null=True),
        ),
    ]