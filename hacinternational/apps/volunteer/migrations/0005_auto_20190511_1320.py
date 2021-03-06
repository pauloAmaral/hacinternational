# Generated by Django 2.1.7 on 2019-05-11 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0004_remove_volunteeropportunity_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteeropportunity',
            name='duration',
            field=models.CharField(choices=[('short_term', 'Short Term'), ('long_term', 'Long Term')], default='short_term', help_text='How long the volunteering opportunity will take', max_length=20),
        ),
    ]
