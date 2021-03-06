# Generated by Django 2.1.7 on 2019-05-11 19:31

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, help_text='If not active, it will not be shown on the list of current events')),
                ('title', models.CharField(help_text='Title of the event', max_length=255)),
                ('image', models.ImageField(upload_to='')),
                ('date', models.DateField(help_text='Date of the event', null=True)),
                ('location', models.CharField(help_text='Where the event will take place', max_length=255)),
                ('description', ckeditor.fields.RichTextField(help_text='Description of the event')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
    ]
