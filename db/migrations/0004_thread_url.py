# Generated by Django 3.1.3 on 2020-11-04 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_community_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='url',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]