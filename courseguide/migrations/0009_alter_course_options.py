# Generated by Django 4.2.22 on 2025-07-31 16:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseguide', '0008_holeguide_stroke_index'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created_on']},
        ),
    ]
