# Generated by Django 5.2.2 on 2025-07-10 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_merge_20250708_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebsiteAccess',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_enabled', models.BooleanField(default=False, help_text='Enable access to the main application')),
                ('enabled_date', models.DateTimeField(blank=True, help_text='Date when access was enabled', null=True)),
                ('disabled_date', models.DateTimeField(blank=True, help_text='Date when access was disabled', null=True)),
                ('notes', models.TextField(blank=True, help_text="Admin notes about this user's access")),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='website_access', to='users.user')),
            ],
            options={
                'verbose_name': 'Website Access',
                'verbose_name_plural': 'Website Access',
                'ordering': ['-created_at'],
            },
        ),
    ]
