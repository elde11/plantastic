# Generated by Django 3.0.5 on 2020-05-23 08:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=150, verbose_name='Description')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=150, verbose_name='Description')),
                ('watering_interval', models.PositiveIntegerField(help_text='In seconds', verbose_name='Watering interval')),
                ('fertilizing_interval', models.PositiveIntegerField(help_text='In seconds', verbose_name='Fertilizing interval')),
                ('required_exposure', models.CharField(choices=[('dark', 'Dark'), ('shade', 'Shade'), ('partsun', 'Part sun'), ('fullsun', 'Full sun')], max_length=10, verbose_name='Amount of sun')),
                ('required_humidity', models.CharField(choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10, verbose_name='Humidity')),
                ('required_temperature', models.CharField(choices=[('cold', 'Cold'), ('medium', 'Medium'), ('warm', 'Warm')], max_length=10, verbose_name='Temperature')),
                ('blooming', models.BooleanField(blank=True, default=False, verbose_name='Blooming?')),
                ('difficulty', models.PositiveIntegerField(choices=[(1, 'Low'), (2, 'Medium-low'), (3, 'Medium'), (4, 'Medium-high'), (5, 'high')], default=1, verbose_name='Cultivation difficulty level')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plants.Category', verbose_name='Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=150, verbose_name='Description')),
                ('exposure', models.CharField(choices=[('dark', 'Dark'), ('shade', 'Shade'), ('partsun', 'Part sun'), ('fullsun', 'Full sun')], max_length=10, verbose_name='Amount of sun')),
                ('humidity', models.CharField(blank=True, choices=[('low', 'Low'), ('medium', 'Medium'), ('high', 'High')], max_length=10, verbose_name='Humidity')),
                ('temperature', models.CharField(blank=True, choices=[('cold', 'Cold'), ('medium', 'Medium'), ('warm', 'Warm')], max_length=10, verbose_name='Temperature')),
                ('drafty', models.BooleanField(blank=True, default=False, verbose_name='Drafty?')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPlant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('description', models.CharField(blank=True, default='', max_length=150, verbose_name='Description')),
                ('image_url', models.URLField(verbose_name='Image URL')),
                ('last_watered', models.DateTimeField(blank=True, null=True, verbose_name='Timestamp of last watering')),
                ('last_fertilized', models.DateTimeField(blank=True, null=True, verbose_name='Timestamp of last fertilizing')),
                ('plant', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plants.Plant', verbose_name='Type of Plant')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='plants.Room', verbose_name='Room')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
