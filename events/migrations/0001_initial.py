# Generated by Django 5.0.1 on 2024-01-09 17:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0003_alter_organizer_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_name', models.CharField(max_length=128)),
                ('place', models.CharField(max_length=32)),
                ('address', models.CharField(max_length=32)),
                ('date_from', models.DateTimeField()),
                ('date_to', models.DateTimeField()),
                ('description', models.TextField()),
                ('capacity', models.IntegerField()),
                ('event_image', models.ImageField(default=None, upload_to='images/')),
                ('event_video', models.CharField(blank=True, max_length=128, null=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='events.category')),
                ('organizer_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='accounts.organizer')),
            ],
        ),
    ]
