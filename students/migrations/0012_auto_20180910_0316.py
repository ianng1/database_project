# Generated by Django 2.0.2 on 2018-09-10 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20180910_0314'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='street',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='street2',
            field=models.CharField(max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='zipcode',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
