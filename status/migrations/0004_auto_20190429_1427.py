# Generated by Django 2.2 on 2019-04-29 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0003_post_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name_plural': 'replies'},
        ),
    ]
