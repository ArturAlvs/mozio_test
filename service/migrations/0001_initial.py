# Generated by Django 2.2.3 on 2019-07-19 03:06

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='provider name.', max_length=50)),
                ('email', models.EmailField(help_text='provider email.', max_length=50)),
                ('phone_number', models.CharField(help_text='provider phone number.', max_length=16)),
                ('language', models.CharField(help_text='provider language.', max_length=25)),
                ('currency', models.CharField(help_text='currency used by provider.', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='service area name.', max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('poly', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Provider')),
            ],
        ),
    ]