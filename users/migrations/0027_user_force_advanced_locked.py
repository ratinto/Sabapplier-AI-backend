# Generated by Django 5.2.2 on 2025-07-16 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0026_alter_user_alt_phone_number_alter_user_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='force_advanced_locked',
            field=models.BooleanField(default=False, help_text='Force advanced features to be locked for this user'),
        ),
    ]
