# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-17 06:46
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('common', '0010_log_commercial_version'),
        ('permission', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updatedatetime', models.DateTimeField(auto_created=True, auto_now=True, verbose_name='Update time')),
                ('createdatetime', models.DateTimeField(auto_now_add=True, verbose_name='Create time')),
                ('groups', models.ManyToManyField(to='common.ServerGroup', verbose_name='Server group')),
                ('permissions', models.ManyToManyField(related_name='rolepermission', to='auth.Permission', verbose_name='Permissions')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='roleuser', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'permissions': (('can_add_user', 'Can add role'), ('can_change_user', 'Can change role info'), ('can_delete_user', 'Can delete role info'), ('can_view_user', 'Can view role info'), ('can_view_permissions', 'Can view role permissions'), ('can_change_permissions', 'Can change role permissions'), ('can_delete_permissions', 'Can revoke role permissions'), ('can_add_permissions', 'Can add role permissions')),
            },
        ),
    ]
