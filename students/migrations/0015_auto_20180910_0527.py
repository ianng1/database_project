# Generated by Django 2.0.2 on 2018-09-10 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0014_auto_20180910_0510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(default='', max_length=35),
        ),
    ]