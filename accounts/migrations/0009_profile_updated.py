# Generated by Django 4.0.4 on 2022-06-16 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_profile_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
    ]
