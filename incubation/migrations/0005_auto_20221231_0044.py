# Generated by Django 3.2.12 on 2022-12-30 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incubation', '0004_auto_20221231_0041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='team',
            old_name='facebook',
            new_name='facebook_link',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='linkedin',
            new_name='linkedin_link',
        ),
        migrations.RenameField(
            model_name='team',
            old_name='twitter',
            new_name='twitter_link',
        ),
    ]
