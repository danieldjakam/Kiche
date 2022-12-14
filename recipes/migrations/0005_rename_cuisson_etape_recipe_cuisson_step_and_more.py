# Generated by Django 4.0.4 on 2034-06-23 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_recipe_ingredients'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='cuisson_etape',
            new_name='cuisson_step',
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='preparation_etape',
            new_name='preparation_step',
        ),
        migrations.AddField(
            model_name='recipe',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='recipes_picture/'),
        ),
    ]
