# Generated by Django 4.1.3 on 2022-12-17 02:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_alter_newsstory_image_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=25)),
                ('description', models.CharField(max_length=254)),
            ],
        ),
    ]
