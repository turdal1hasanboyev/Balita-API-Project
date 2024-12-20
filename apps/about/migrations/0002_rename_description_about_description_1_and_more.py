# Generated by Django 5.1.4 on 2024-12-15 08:41

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='description',
            new_name='description_1',
        ),
        migrations.AddField(
            model_name='about',
            name='description_2',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='description_3',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
