# Generated by Django 4.0.4 on 2022-06-13 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_rename_last_name_profile_family_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='avatars/'),
        ),
    ]
