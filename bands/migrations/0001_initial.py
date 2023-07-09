# Generated by Django 4.2.1 on 2023-07-09 20:25

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('country', models.CharField(blank=True, max_length=150)),
                ('city', models.CharField(blank=True, max_length=150)),
                ('members', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, max_length=1000), size=None)),
                ('image', models.CharField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True)),
                ('year', models.CharField(max_length=4)),
                ('color', models.CharField(blank=True)),
                ('tracklist', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True), size=None)),
                ('country', models.CharField(blank=True)),
                ('genre', models.CharField(blank=True)),
                ('image', models.CharField(blank=True)),
                ('on_sale', models.BooleanField(blank=True, null=True)),
                ('artist', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='releases', to='bands.band')),
                ('variants', models.ManyToManyField(blank=True, to='bands.album')),
            ],
        ),
    ]
