# Generated by Django 2.1.7 on 2019-05-08 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerOpportunity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True, help_text='If not active, it will not show on the list of opportunities')),
                ('title', models.CharField(help_text='Main title for the volunteering opportunity', max_length=255)),
                ('location', models.CharField(help_text='Where the volunteering opportunity will take place', max_length=255)),
                ('time', models.CharField(help_text='When the volunteering opportunity will take place', max_length=255)),
                ('description', models.CharField(help_text='What the volunteer will need to do', max_length=500)),
                ('volunteer_profile', models.CharField(help_text='What kind of volunteer we are looking for', max_length=500, null=True)),
                ('reason', models.CharField(help_text='Why this is important', max_length=500, null=True)),
                ('rewards', models.CharField(help_text='What the volunteer will get for doing this', max_length=500, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
