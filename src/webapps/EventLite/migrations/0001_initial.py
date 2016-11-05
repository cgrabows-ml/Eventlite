# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-11-04 21:53
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Buyer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numOfTickets', models.IntegerField(default=0)),
                ('ticketsSold', models.IntegerField(default=0)),
                ('description', models.CharField(blank=True, default=b'', max_length=1000)),
                ('location', models.CharField(blank=True, default=b'', max_length=100)),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('media', models.URLField(blank=True, default=b'')),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to=b'images')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventLite.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('review', models.CharField(blank=True, default=b'', max_length=420)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventLite.Event')),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('earnings', models.FloatField(default=0.0)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField()),
                ('details', models.CharField(max_length=1000)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventLite.Event')),
            ],
        ),
        migrations.CreateModel(
            name='UserDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=b'icons')),
                ('bio', models.CharField(blank=True, default=b'', max_length=420, null=True)),
                ('social_login', models.BooleanField()),
                ('buyer', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EventLite.Buyer')),
                ('seller', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='EventLite.Seller')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='seller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EventLite.Seller'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='eventsInterested',
            field=models.ManyToManyField(blank=True, to='EventLite.Event'),
        ),
        migrations.AddField(
            model_name='buyer',
            name='ticketsPurchased',
            field=models.ManyToManyField(blank=True, to='EventLite.Ticket'),
        ),
    ]
