# Generated by Django 4.0.4 on 2022-05-12 14:16

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_post_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='picture',
            field=sorl.thumbnail.fields.ImageField(null=True, upload_to='img/', verbose_name='概述图片'),
        ),
    ]
