# Generated by Django 3.2.12 on 2022-12-30 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubation', '0005_auto_20221231_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='facebook_link',
            field=models.URLField(blank=True, default='raise.recb.ac.in', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='linkedin_link',
            field=models.URLField(blank=True, default='raise.recb.ac.in', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='team',
            name='twitter_link',
            field=models.URLField(blank=True, default='raise.recb.ac.in', max_length=1000, null=True),
        ),
    ]