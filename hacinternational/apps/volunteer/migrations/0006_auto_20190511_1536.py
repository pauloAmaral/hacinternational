# Generated by Django 2.1.7 on 2019-05-11 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0005_auto_20190511_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteeropportunity',
            name='description',
            field=models.CharField(help_text='What the volunteer will need to do', max_length=1500),
        ),
    ]
