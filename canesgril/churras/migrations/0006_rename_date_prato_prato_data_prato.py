# Generated by Django 5.2.3 on 2025-07-12 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('churras', '0005_rename_data_prato_prato_date_prato_prato_foto_prato_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prato',
            old_name='date_prato',
            new_name='data_prato',
        ),
    ]
