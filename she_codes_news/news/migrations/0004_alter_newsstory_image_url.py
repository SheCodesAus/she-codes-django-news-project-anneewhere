# Generated by Django 4.1.3 on 2022-12-16 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_alter_newsstory_options_newsstory_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(),
        ),
    ]