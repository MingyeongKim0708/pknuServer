# Generated by Django 3.1.3 on 2022-01-10 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0004_auto_20220110_1111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='answer',
            old_name='modified_date',
            new_name='modify_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='modified_date',
            new_name='modify_date',
        ),
    ]