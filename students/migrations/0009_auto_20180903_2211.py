# Generated by Django 2.0.2 on 2018-09-03 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0008_auto_20180826_2346'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='activity',
            field=models.CharField(max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='level',
            field=models.CharField(max_length=25, null=True),
        ),
    ]