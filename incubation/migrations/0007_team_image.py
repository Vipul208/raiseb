# Generated by Django 3.2.12 on 2022-12-30 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incubation', '0006_auto_20221231_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='image',
            field=models.ImageField(blank=True, default='Image/profile1.png', null=True, upload_to='Team'),
        ),
    ]
