# Generated by Django 3.1.3 on 2020-11-04 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_thread_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='title',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
