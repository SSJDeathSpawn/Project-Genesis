# Generated by Django 2.2 on 2019-04-29 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0002_reply_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(null=True, verbose_name='date published'),
        ),
    ]
